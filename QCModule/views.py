from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import pandas as pd
from django.conf import settings
import sqlalchemy
import os
import json
from django.http import JsonResponse
import requests
from datetime import datetime
df=pd.DataFrame()

def index(request):
    global df
    arg = {"header": df.columns, "data": df.values.tolist(), "select": "YVROKAR"}
    # return render(request, 'Operations/dryout.html', arg)
    return render(request,'QCModule/qc.html', arg)


def Upload(request):
    df_list=[]
    global df
    if request.user.is_superuser: #True:
        print("super user")
        if "GET" == request.method:
            return render(request,'QCModule/upload.html')
        elif request.method=='POST' and 'qcfile' in request.FILES:
            # Here it is already not empty, and you can attach
            excel_file1 = request.FILES.getlist('qcfile')
            # for i in excel_file1: # uploaded ecel file to pandas dataframe
            #     print(i)
            #     df = pd.DataFrame()
            #     if str(i).lower().endswith('.csv'):
            #         df = pd.read_csv(i, index_col=False)
            #     elif str(i).lower().endswith(('.xls', '.xlsx')):
            #         sheets=pd.read_excel(i,sheet_name=None)
            #         df = pd.concat(sheets[frame] for frame in sheets.keys())
            #     df_list.append(df)
            df = pd.read_excel(excel_file1[0])
            boolean = df['Tank'].isna()
            df = df[~boolean]
            df["QtyDiff"] =df["Physical Balance"] - df["Quantity"]
            df["QtyDiff"]=df["QtyDiff"].map(lambda x:round(x,2))
            df["Status"] = df["QtyDiff"].map(lambda x: "Dormant" if abs(x) < 10 else ("Receipt" if x > 10 else "Dispatch"))
            print(df)
            if False: # upload excel file to mySQL database.efficent method
                user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']
                database_url = 'mysql+pymysql://{user}:{password}@localhost:3306/{database_name}'.format(user=user,password=password,database_name=database_name)
                engine = sqlalchemy.create_engine(database_url) #, echo=False
                # for df in df_list:
                #     # df['id']=df.index
                #     for j,column in enumerate(Columns):
                #         if set(column).issubset(df.columns):
                #             Models[j].objects.all().delete() # delete selected SQL table values
                #             df.to_sql(Models[j]._meta.db_table, con=engine,index=False,if_exists='replace') #replace, fail,append ,index=False
            arg={"success":"Data uploaded successfully..."}
            return render(request,'QCModule/upload.html',arg)

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print("user=",user)
        if user is not None:
            auth.login(request,user)
            return redirect("/qc/index")
        else:
            messages.info(request,'invalid credentials')
            return render(request,'QCModule/login.html')
    else:
        return render(request,'QCModule/login.html')
def logout(request):
    auth.logout(request)
    return redirect("/qc")