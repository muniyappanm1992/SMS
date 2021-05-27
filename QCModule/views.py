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
from .columns import Columns,yqlabColumn,yvrokarColumn
from .models import Models, yvrokarModel, yqlabModel


def index(request):
    df_list=[]
    if request.user.is_authenticated: #True:
        print("is_authenticated",request.user.is_authenticated)
        from django.utils import timezone
        now = timezone.localtime(timezone.now())
        current_date=now.strftime("%d-%m-%Y")
        current_time=now.strftime("%H%M")
        print(request.POST)
        if "GET" == request.method:
            return render(request, 'QCModule/index.html')
        elif request.method == 'POST' and 'qcfile' in request.FILES:
            df_yvrokar = pd.DataFrame()
            df_yqlab = pd.DataFrame()
            df_read = pd.DataFrame()
            # Here it is already not empty, and you can attach
            excel_file1 = request.FILES.getlist('qcfile')
            for i in excel_file1:  # uploaded ecel file to pandas dataframe
                print(i)
                if str(i).lower().endswith('.csv'):
                    df_read = pd.read_csv(i, index_col=False)
                elif str(i).lower().endswith(('.xls', '.xlsx')):
                    sheets = pd.read_excel(i, sheet_name=None)
                    df_read = pd.concat(sheets[frame] for frame in sheets.keys())
                df_list.append(df_read)
            for x in df_list:
                if {'Material', 'Tank', 'Tank Status', 'Opening Dip',
                    'Book Balance', 'Closing Dip', 'Physical Balance', 'Loss/Gain'}.issubset(
                    x.columns):
                    print('entered')
                    df_yvrokar = x.copy()
                    boolean = df_yvrokar['Tank'].isna()
                    df_yvrokar = df_yvrokar[~boolean]
                    df_yvrokar["QtyDiff"] = df_yvrokar["Physical Balance"] - df_yvrokar["Quantity"]
                    df_yvrokar["QtyDiff"] = df_yvrokar["QtyDiff"].map(lambda x: round(x, 2))
                    df_yvrokar["Status"] = df_yvrokar["QtyDiff"].map(
                        lambda x: "Dormant" if abs(x) < 10 else ("Receipt" if x > 10 else "Dispatch"))
                    print(df_yvrokar.columns)
                elif {'Lab Register No.', 'Plant', 'Material', 'Storage Tank',
                      'Test Laboratory', 'Inspection Lot'}.issubset(
                    x.columns):
                    df_yqlab = x.copy()
            df = pd.merge(left=df_yvrokar, right=df_yqlab, how='inner',
                              left_on=['Tank', 'Material'], right_on=['Storage Tank', 'Material'])
            arg = {"header": df.columns, "data": df.values.tolist(), "select": "QC Dashboard"}
            return render(request, 'QCModule/qc.html', arg)
        elif request.method == 'POST':
            df_yvrokar = pd.DataFrame()
            df_yqlab = pd.DataFrame()
            user = settings.DATABASES['default']['USER']
            password = settings.DATABASES['default']['PASSWORD']
            database_name = settings.DATABASES['default']['NAME']
            database_url = 'mysql+pymysql://{user}:{password}@localhost:3306/{database_name}'.format(user=user,
                                                                                                     password=password,
                                                                                                     database_name=database_name)
            engine = sqlalchemy.create_engine(database_url)  # , echo=False
            df_yvrokar=pd.read_sql('select * from {0}.{1}'.format(database_name, yvrokarModel._meta.db_table), con=engine)
            df_yqlab = pd.read_sql('select * from {0}.{1}'.format(database_name, yqlabModel._meta.db_table),con=engine)
            df = pd.merge(left=df_yvrokar, right=df_yqlab, how='inner',
                          left_on=['Tank','Material'], right_on=['Storage Tank','Material'])
            arg = {"header": df.columns, "data": df.values.tolist(), "select": "QC Dashboard"}
            return render(request, 'QCModule/qc.html', arg)

    else:
        messages.info(request, 'invalid credentials')
        return render(request, 'QCModule/login.html')


def Upload(request):
    df_list=[]
    df_category=[]
    if request.user.is_superuser: #True:
        print("super user")
        if "GET" == request.method:
            return render(request,'QCModule/upload.html')
        elif request.method=='POST' and 'qcfile' in request.FILES:
            # Here it is already not empty, and you can attach
            excel_file1 = request.FILES.getlist('qcfile')
            for i in excel_file1: # uploaded ecel file to pandas dataframe
                print(i)
                if str(i).lower().endswith('.csv'):
                    df_read = pd.read_csv(i, index_col=False)
                elif str(i).lower().endswith(('.xls', '.xlsx')):
                    sheets=pd.read_excel(i,sheet_name=None)
                    df_read = pd.concat(sheets[frame] for frame in sheets.keys())
                df_list.append(df_read)
            for x in df_list:
                if { 'Material', 'Tank', 'Tank Status', 'Opening Dip',
                    'Book Balance','Closing Dip','Physical Balance','Loss/Gain'}.issubset(
                        x.columns):
                    df_yvrokar = x.copy()
                    boolean = df_yvrokar['Tank'].isna()
                    df_yvrokar = df_yvrokar[~boolean]
                    df_yvrokar["QtyDiff"] = df_yvrokar["Physical Balance"] - df_yvrokar["Quantity"]
                    df_yvrokar["QtyDiff"] = df_yvrokar["QtyDiff"].map(lambda x: round(x, 2))
                    df_yvrokar["Status"] = df_yvrokar["QtyDiff"].map(
                        lambda x: "Dormant" if abs(x) < 10 else ("Receipt" if x > 10 else "Dispatch"))
                    df_category.append(df_yvrokar)
                    print(df_yvrokar.columns)
                elif { 'Lab Register No.', 'Plant', 'Material', 'Storage Tank',
                    'Test Laboratory','Inspection Lot'}.issubset(
                        x.columns):
                    df_yqlab = x.copy()
                    df_category.append(df_yqlab)
                    print(df_yqlab.columns)
                    print(Columns[1])
            if True: # upload excel file to mySQL database.efficent method
                user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']
                database_url = 'mysql+pymysql://{user}:{password}@localhost:3306/{database_name}'.format(user=user,password=password,database_name=database_name)
                engine = sqlalchemy.create_engine(database_url) #, echo=False
                for df in df_category:
                    for j,column in enumerate(Columns):
                        if set(df.columns).issubset(column):
                            print("Column match {0}    ".format(Columns.index(column)),column)
                            Models[j].objects.all().delete() # delete selected SQL table values
                            df.to_sql(Models[j]._meta.db_table, con=engine,index=False,if_exists='replace') #replace, fail,append ,index=False
            arg={"success":"Data uploaded successfully..."}
            return render(request,'QCModule/upload.html',arg)
    else:
        messages.info(request, 'invalid credentials')
        return render(request, 'QCModule/login.html')
def login(request):
    if request.user.is_authenticated:
        return redirect("/qc/index")
    elif request.method=='POST':
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
    return redirect("/")