from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import pandas as pd
import os
import json
from django.http import JsonResponse
import requests
from datetime import datetime
from .models import Models,godryModel,outofstockModel,romobileModel,rolistModel,yv26Model,yv208Model,yv209dModel
from django_pandas.io import read_frame
from .column import Columns,godryColumn,outofstockColumn,romobileColumn,rolistColumn,yv26Column,yv208Column,yv209dColumn,HTMLColumn,MaterialCode,MaterianDescription,\
sheet_names,select,website
def Dryout(dryout_df=pd.DataFrame(),yv209d_df=pd.DataFrame(),yv208_df=pd.DataFrame(),yv26_df=pd.DataFrame(),rolist_df=pd.DataFrame(),sql=True):
    def Code2Description(df,columnName,Material=MaterialCode,Description=MaterianDescription):
        df.replace({columnName: Material}, {columnName: Description}, regex=True,inplace=True)
    if True: # yv26 block
        if sql:
            yv26_df=read_frame(yv26Model.objects.all(),index_col='id')
        yv26_df=yv26_df[['Rec. Code','Receiver','Mat.Code','Volume(KL)','PGI Date','InvoiceNo.']]
        yv26_df['Mat.Code']=yv26_df['Mat.Code'].astype('str')
        Code2Description(yv26_df,'Mat.Code')
        yv26_df['Rec. Code']=yv26_df['Rec. Code'].astype('str')
        yv26_df['Rec. Code']=yv26_df['Rec. Code'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
    if True: # dryout block
        if sql:
            godry_df=read_frame(godryModel.objects.all(),index_col='id')
            outofstock_df=read_frame(outofstockModel.objects.all(),index_col='id')
            outofstock_df['STATUS CRITICAL'] = 'Out of Stock'
            dryout_df = pd.concat([godry_df, outofstock_df], ignore_index=True)
        dryout_df=dryout_df[['DO NAME','RO CODE','RO NAME','PRODUCT','STATUS CRITICAL','EXPECTED DRYOUT DATE/ TIME']] #'SUPPLY LOCATION','EXPECTED DRYOUT DATE/ TIME','TRANSIT TIME (HRS.)','STOCK SURVIVAL HOURS (HRS.)'
        dryout_df['RO CODE']=dryout_df['RO CODE'].astype('str')
        dryout_df['RO CODE']=dryout_df['RO CODE'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
        dryout_df['RO-PRODUCT'] = dryout_df['RO CODE'] + '-' + +dryout_df['PRODUCT'].astype('str')
    if True: # yv209d block
        if sql:
            yv209d_df=read_frame(yv209dModel.objects.all(),index_col='id')
        yv209d_df=yv209d_df[['Ship2Party','Name 1','RTD(in KM)','REMARKS','Sales Document','Material']]
        yv209d_df['Material']=yv209d_df['Material'].astype('str')
        Code2Description(yv209d_df,'Material')
        yv209d_df['Ship2Party']=yv209d_df['Ship2Party'].astype('str')
        yv209d_df['Ship2Party']=yv209d_df['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
    if True: # yv208 block   
        if sql: 
            yv208_df=read_frame(yv208Model.objects.all(),index_col='id')
        yv208_df=yv208_df[['Material','Vehicle','Ship2Party','Name','Invoice']]
        yv208_df['Material']=yv208_df['Material'].astype('str')
        Code2Description(yv208_df,'Material')
        yv208_df['Ship2Party']=yv208_df['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
        yv208_df['Ship2Party']=yv208_df['Ship2Party'].astype('str')
    if True: # rolist block
        if sql:
            rolist_df=read_frame(rolistModel.objects.all(),index_col='id')
        rolist_df['Ship2Party']=rolist_df['Ship2Party'].map(lambda x:"0000"+str(x))
    df_yv209dpending=pd.merge(left=dryout_df,right=yv209d_df,how='inner',left_on=['RO CODE','PRODUCT'],right_on=['Ship2Party','Material'])
    df_yv208planned=pd.merge(left=dryout_df,right=yv208_df,how='inner',left_on=['RO CODE','PRODUCT'],right_on=['Ship2Party','Material'])
    df_yv208planned['Invoice']=df_yv208planned['Invoice'].astype('str')
    df_yv208planned['Invoice']=df_yv208planned['Invoice'].map(lambda x:x if len(x)>4 else "Planned/UnderLoading")
    df_plan=df_yv208planned[df_yv208planned['Invoice']=="Planned/UnderLoading"]
    df_invoiced=df_yv208planned[df_yv208planned['Invoice']!="Planned/UnderLoading"]
    print(df_yv208planned)
    df_con=pd.concat([df_yv209dpending[['DO NAME','RO CODE','RO NAME','PRODUCT','STATUS CRITICAL']],df_yv208planned[['DO NAME','RO CODE','RO NAME','PRODUCT','STATUS CRITICAL']]],ignore_index=True)
    df_con['RO-PRODUCT'] = df_con['RO CODE'] + '-' + +df_con['PRODUCT'].astype('str')
    boolen_series=dryout_df['RO-PRODUCT'].isin(df_con['RO-PRODUCT'].values.tolist())
    df_filter=dryout_df[~boolen_series]
    df_noindent=pd.merge(left=df_filter,right=rolist_df,how='inner',left_on=['RO CODE'],right_on=['Ship2Party'])
    df_noindent["ROMaterial"]=df_noindent["RO CODE"].astype('str')+df_noindent["PRODUCT"].astype('str')
    yv26_df["ROMaterial"]=yv26_df["Rec. Code"].astype('str')+yv26_df["Mat.Code"].astype('str')
    boolen_yv26=df_noindent['ROMaterial'].isin(yv26_df['ROMaterial'].values.tolist())
    df_yesterdaysupplied=pd.merge(left=df_noindent,right=yv26_df,how='inner',left_on=['RO CODE','PRODUCT'],right_on=['Rec. Code','Mat.Code'])
    df_noindent=df_noindent[~boolen_yv26]
    print("List===",[df_yv209dpending,df_plan,df_invoiced,df_yesterdaysupplied,df_noindent])
    return [df_yv209dpending,df_plan,df_invoiced,df_yesterdaysupplied,df_noindent]
def index(request):
    df_out_of_stock = pd.DataFrame()
    df_about_to_dry = pd.DataFrame()
    df_yv209d = pd.DataFrame()
    df_yv208 = pd.DataFrame()
    df_yv26 = pd.DataFrame()
    df_yv207 = pd.DataFrame()
    df_ROlist = pd.DataFrame()
    df_Phone=pd.DataFrame()
    df_list = []
    df_DryoutExport=[]
    if request.user.is_authenticated: #True:
        print("is_authenticated",request.user.is_authenticated)
        now=datetime.now()
        current_date=now.strftime("%d-%m-%Y")
        current_time=now.strftime("%H%M")
        print(request.POST)
        if "GET" == request.method:
            return render(request, 'index.html')
        elif request.method=='POST' and 'dryout' in request.FILES:
            # Here it is already not empty, and you can attach
            excel_file1 = request.FILES.getlist('dryout')
            for i in excel_file1: # uploaded ecel file to pandas dataframe
                print(i)
                df = pd.DataFrame()
                if str(i).lower().endswith('.csv'):
                    df = pd.read_csv(i, index_col=False)
                elif str(i).lower().endswith(('.xls', '.xlsx')):
                    sheets=pd.read_excel(i,sheet_name=None)
                    df = pd.concat(sheets[frame] for frame in sheets.keys())
                df_list.append(df)
            if False: # delete all SQL table values
                for Model in Models:
                    Model.objects.all().delete()
            if False: # upload excel file to mySQL database.
                for df in df_list:
                    for column in Columns:  
                        if set(column).issubset(df.columns):
                            if Columns.index(column)==0:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i],df[Columns[j][14]][i],\
                                    df[Columns[j][15]][i],df[Columns[j][16]][i],df[Columns[j][17]][i],df[Columns[j][18]][i],df[Columns[j][19]][i])
                                    value.save()
                            elif Columns.index(column)==1:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i])
                                    value.save()    
                            elif Columns.index(column)==2:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i])
                                    value.save()
                            elif Columns.index(column)==3:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i])
                                    value.save()
                            elif Columns.index(column)==4:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i],df[Columns[j][14]][i],\
                                    df[Columns[j][15]][i],df[Columns[j][16]][i],df[Columns[j][17]][i],df[Columns[j][18]][i],df[Columns[j][19]][i],df[Columns[j][20]][i])
                                    value.save()  
                            elif Columns.index(column)==5:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i])
                                    value.save()
                            elif Columns.index(column)==6:
                                j=Columns.index(column);
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i],df[Columns[j][14]][i],\
                                    df[Columns[j][15]][i],df[Columns[j][16]][i],df[Columns[j][17]][i],df[Columns[j][18]][i])
                                    value.save()
            if False: # read data from mySQL database to pandas dataframe
                df=read_frame(yv208Model.objects.all(),index_col='id')
            # return render(request, 'index.html')   
            for x in df_list:                               
                if {'SO NAME', 'DO NAME', 'SALES AREA', 'RO CODE', 'RO NAME', 'PRODUCT',
                    'TOTAL HOURS STOCK OUT'}.issubset(
                        x.columns):
                    df_out_of_stock = x.copy()
                    df_out_of_stock['STATUS CRITICAL'] = 'Out of Stock'
                    df_out_of_stock['RO CODE'] = df_out_of_stock['RO CODE'].map(str)
                    df_out_of_stock['PRODUCT'] = df_out_of_stock['PRODUCT'].map(str)
                    df_out_of_stock['RO CODE'] = df_out_of_stock['RO CODE'].map(
                        lambda m: '0000' + str(m) if len(m) < 8 else m)
                    df_out_of_stock['RO-PRODUCT'] = df_out_of_stock['RO CODE'] + '-' + +df_out_of_stock['PRODUCT']
                    df_out_of_stock['EXPECTED DRYOUT DATE/ TIME']="NA"
                    df_out_of_stock = df_out_of_stock[
                        ['SO NAME', 'DO NAME', 'SALES AREA', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS CRITICAL',
                            'RO-PRODUCT','EXPECTED DRYOUT DATE/ TIME']]
                elif {'SO NAME', 'DO NAME', 'SALES AREA', 'RO CODE', 'RO NAME', 'PRODUCT', 'EXPECTED DRYOUT DATE/ TIME',
                        'STATUS CRITICAL'}.issubset(x.columns):
                    df_about_to_dry = x.copy()
                    df_about_to_dry['RO CODE'] = df_about_to_dry['RO CODE'].map(str)
                    df_about_to_dry['PRODUCT'] = df_about_to_dry['PRODUCT'].map(str)
                    df_about_to_dry['RO CODE'] = df_about_to_dry['RO CODE'].map(
                        lambda m: '0000' + str(m) if len(m) < 8 else m)
                    df_about_to_dry['RO-PRODUCT'] = df_about_to_dry['RO CODE'] + '-' + +df_about_to_dry['PRODUCT']
                    df_about_to_dry = df_about_to_dry[
                        ['SO NAME', 'DO NAME', 'SALES AREA', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS CRITICAL',
                            'RO-PRODUCT','EXPECTED DRYOUT DATE/ TIME']]
                elif {'Ship2Party', 'Sales Document', 'REMARKS', 'Name 1'}.issubset(x.columns):
                    df=x.copy()
                    df['Ship2Party']=df['Ship2Party'].astype('str')
                    df['Ship2Party']=df['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
                    df_yv209d = df.copy()
                elif {'Ship2Party', 'Shipment', 'Shp.Status', 'Vehicle'}.issubset(x.columns):
                    df=x.copy()
                    df['Ship2Party']=df['Ship2Party'].astype('str')
                    df['Ship2Party']=df['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
                    df_yv208 = df.copy()
                elif {'Rec. Code', 'Receiver', 'Document', 'InvoiceNo.'}.issubset(x.columns):
                    df_yv26 = x.copy()
                elif {'Ship2Party', 'Name', 'SOff.','Rg'}.issubset(x.columns):
                    df_ROlist = x.copy()
                elif {'Mobile Number', 'Ship-To Party', 'Sales Office','Mobile Type','Distribution Channel'}.issubset(x.columns):
                    df=x.copy()
                    df['Ship-To Party']=df['Ship-To Party'].astype('str')
                    df['Ship-To Party']=df['Ship-To Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
                    df_Phone = df.copy()
            dryout_df = pd.concat([df_about_to_dry, df_out_of_stock], ignore_index=True)
            df_DryoutExport=Dryout(dryout_df,df_yv209d,df_yv208,df_yv26,df_ROlist,False).copy()
            if 'export' in request.POST: # export dryout list in excel and download in local machine
                with BytesIO() as b:
                    writer = pd.ExcelWriter(b, engine='xlsxwriter')
                    for i, df_excel in enumerate(df_DryoutExport):
                        df_excel.to_excel(writer, sheet_name=sheet_names[i], index=False)
                        # Indicate workbook and worksheet for formatting
                        workbook = writer.book
                        worksheet = writer.sheets[sheet_names[i]]
                        formater = workbook.add_format({'border': 1})
                        # Iterate through each column and set the width == the max length in that column. A padding length of 2
                        # is also added.
                        for j, col in enumerate(df_excel.columns):
                            # find length of column i
                            column_len = df_excel[col].astype(str).str.len().max()
                            # Setting the length if the column header is larger
                            # than the max column value length
                            column_len = max(column_len, len(col)) + 2
                            # set the column length
                            worksheet.set_column(j, j, column_len, formater)
                    writer.save()
                    response = HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')
                    response['Content-Disposition'] = 'attachment; filename="dryout status at {0} hrs on {1}.xlsx"'.format(current_time,current_date)
                    return response
                    # return render(request, 'index.html')
            elif 'select' in request.POST: # table web view
                global select
                df_DryoutExport.append(df_yv209d)
                df_DryoutExport.append(df_yv208)
                left=['RO CODE','RO CODE','RO CODE','RO CODE','RO CODE','Ship2Party','Ship2Party']
                sms_tables=["YV209D-dryout",'No indent','YV209D']
                selected_list = request.POST.get('select')
                df=pd.merge(left=df_DryoutExport[select.index(selected_list)],right=df_Phone,how='inner',left_on=[left[select.index(selected_list)]],right_on=['Ship-To Party'])
                df=df[HTMLColumn[select.index(selected_list)]]
                if set([selected_list]).issubset(set(sms_tables)):
                    df['SMS']="SMS"
                arg={"header":df.columns,"data":df.values.tolist(),"select":selected_list}
                return render(request, 'dryout.html',arg)
            else:
                return render(request, 'index.html')
        elif request.method=='POST' and 'dryout' not in request.FILES:
            df_nodry=Dryout().copy()
            if 'export' in request.POST: # export dryout list in excel and download in local machine
                with BytesIO() as b:
                    writer = pd.ExcelWriter(b, engine='xlsxwriter')
                    for i, df_excel in enumerate(df_nodry):
                        df_excel.to_excel(writer, sheet_name=sheet_names[i], index=False)
                        # Indicate workbook and worksheet for formatting
                        workbook = writer.book
                        worksheet = writer.sheets[sheet_names[i]]
                        formater = workbook.add_format({'border': 1})
                        # Iterate through each column and set the width == the max length in that column. A padding length of 2
                        # is also added.
                        for j, col in enumerate(df_excel.columns):
                            # find length of column i
                            column_len = df_excel[col].astype(str).str.len().max()
                            # Setting the length if the column header is larger
                            # than the max column value length
                            column_len = max(column_len, len(col)) + 2
                            # set the column length
                            worksheet.set_column(j, j, column_len, formater)
                    writer.save()
                    response = HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')
                    response['Content-Disposition'] = 'attachment; filename="dryout status at {0} hrs on {1}.xlsx"'.format(current_time,current_date)
                    return response
                    # return render(request, 'index.html')
            elif 'select' in request.POST: # table web view
                left=['RO CODE','RO CODE','RO CODE','RO CODE','RO CODE','Ship2Party','Ship2Party']
                sms_tables=["YV209D-dryout",'No indent','YV209D']
                selected_list = request.POST.get('select')
                df_nodry.append(read_frame(yv209dModel.objects.all(),index_col='id'))
                df_nodry[-1]['Ship2Party']=df_nodry[-1]['Ship2Party'].astype('str')
                df_nodry[-1]['Ship2Party']=df_nodry[-1]['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
                df_nodry.append(read_frame(yv208Model.objects.all(),index_col='id'))
                df_nodry[-1]['Ship2Party']=df_nodry[-1]['Ship2Party'].astype('str')
                df_nodry[-1]['Ship2Party']=df_nodry[-1]['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
                df_Phone=read_frame(romobileModel.objects.all(),index_col='id')
                df_Phone['Ship-To Party']=df_Phone['Ship-To Party'].astype('str')
                df_Phone['Ship-To Party']=df_Phone['Ship-To Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
                print(select)
                print("df_nodry=",df_nodry[select.index(selected_list)])
                df=pd.merge(left=df_nodry[select.index(selected_list)],right=df_Phone,how='inner',left_on=[left[select.index(selected_list)]],right_on=['Ship-To Party'])
                df=df[HTMLColumn[select.index(selected_list)]]
                if set([selected_list]).issubset(set(sms_tables)):
                    df['SMS']="SMS"
                arg={"header":df.columns,"data":df.values.tolist(),"select":selected_list}
                return render(request, 'dryout.html',arg)
    else:
        messages.info(request, 'Please login first..')
        return redirect("/")
def Muni(request):
    print(request.POST)
    if  'array[]' in request.POST:
        array = request.POST.getlist('array[]')
        title=request.POST.get('title')
        print("title",title)
        global select,website
        ind=select.index(title)
        print(HTMLColumn[ind])
        dictionary = dict(zip(HTMLColumn[ind], array))
        MobileNumber=dictionary['Mobile Number']
        # MobileNumber=917093890777
        ### SMS #################
        mobileno=[]
        if title=='YV209D':
            message = "Dear {0}, Your SO no:{1} cannot be processed due to {2}. More information visit {3}. IOCL SALEM Terminal- MUNIYAPPAN".format("("+dictionary['Ship2Party']+") "+dictionary['Name 1_x'],dictionary['Sales Document'],dictionary['REMARKS'],website)
        elif title=="YV209D-dryout":
                message = "Dear {0}, Your SO no:{1} cannot be processed due to {2}. More information visit {3}. IOCL SALEM Terminal- MUNIYAPPAN".format("("+dictionary['RO CODE']+") "+dictionary['RO NAME'],dictionary['Sales Document'],dictionary['REMARKS'],website)
        elif title=='No indent':
                message = "Dear {0}, Your RO is about to go dry for {1} at {2}.You are requested to place indent immediately to avoid dryout please . More info visit {3}. IOCL SALEM- MUNIYAPPAN".format("("+dictionary['RO CODE']+") "+dictionary['RO NAME'],dictionary['PRODUCT'],dictionary['EXPECTED DRYOUT DATE/ TIME'],website)
        mobileno.append('{0}'.format(MobileNumber))
        print("message= ",message)
        print("MobileNumber= ",MobileNumber)
        # mobileno.append('918870887201') #919442613017 #918985534670
        sender = 'MUNIMM'
        apikey = '1025ci03w5o077767a02l983n405q4620ne'
        baseurl = 'https://instantalerts.co/api/web/send/?apikey='+apikey
        print(baseurl)
        for mobile in mobileno:
            url= baseurl+'&sender='+sender+'&to='+mobile+'&message='+message+'&format=json'
            print(url)
            response = requests.get(url)
            print(response.json())
            # Check for HTTP codes other than 200
            if response.status_code != 200:
                print('Status:', response, 'Problem with the request.')
            ### SMS #################
            data = {'code': 'Success'}
            js_data = json.dumps(data)
        return JsonResponse(data)
def Upload(request):
    df_list=[]
    if request.user.is_superuser: #True:
        print("super user")
        if "GET" == request.method:
            return render(request,'upload.html')
        elif request.method=='POST' and 'dryout' in request.FILES:
            # Here it is already not empty, and you can attach
            excel_file1 = request.FILES.getlist('dryout')
            for i in excel_file1: # uploaded ecel file to pandas dataframe
                print(i)
                df = pd.DataFrame()
                if str(i).lower().endswith('.csv'):
                    df = pd.read_csv(i, index_col=False)
                elif str(i).lower().endswith(('.xls', '.xlsx')):
                    sheets=pd.read_excel(i,sheet_name=None)
                    df = pd.concat(sheets[frame] for frame in sheets.keys())
                df_list.append(df)
            if False: # delete all SQL table values
                for Model in Models:
                    Model.objects.all().delete()
            if True: # upload excel file to mySQL database.
                for df in df_list:
                    for column in Columns:  
                        if set(column).issubset(df.columns):
                            if Columns.index(column)==0:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i],df[Columns[j][14]][i],\
                                    df[Columns[j][15]][i],df[Columns[j][16]][i],df[Columns[j][17]][i],df[Columns[j][18]][i],df[Columns[j][19]][i])
                                    value.save()
                            elif Columns.index(column)==1:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i])
                                    value.save()    
                            elif Columns.index(column)==2:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i])
                                    value.save()
                            elif Columns.index(column)==3:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i])
                                    value.save()
                            elif Columns.index(column)==4:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i],df[Columns[j][14]][i],\
                                    df[Columns[j][15]][i],df[Columns[j][16]][i],df[Columns[j][17]][i],df[Columns[j][18]][i],df[Columns[j][19]][i],df[Columns[j][20]][i])
                                    value.save()  
                            elif Columns.index(column)==5:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i])
                                    value.save()
                            elif Columns.index(column)==6:
                                j=Columns.index(column);
                                Models[j].objects.all().delete() # delete selected SQL table values
                                for i,data in enumerate(df.values.tolist()):
                                    value=Models[j](i+1,df[Columns[j][0]][i],df[Columns[j][1]][i],df[Columns[j][2]][i],df[Columns[j][3]][i],\
                                    df[Columns[j][4]][i],df[Columns[j][5]][i],df[Columns[j][6]][i],df[Columns[j][7]][i],df[Columns[j][8]][i],\
                                    df[Columns[j][9]][i],df[Columns[j][10]][i],df[Columns[j][11]][i],df[Columns[j][12]][i],df[Columns[j][13]][i],df[Columns[j][14]][i],\
                                    df[Columns[j][15]][i],df[Columns[j][16]][i],df[Columns[j][17]][i],df[Columns[j][18]][i])
                                    value.save()
            if False: # read data from mySQL database to pandas dataframe
                df=read_frame(yv208Model.objects.all(),index_col='id')
            arg={"success":"Data uploaded susuccessfully..."}           
            return render(request,'upload.html',arg)
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print("user=",user)
        if user is not None:
            auth.login(request,user)
            return redirect("/index")
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")