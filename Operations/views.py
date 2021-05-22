from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import pandas as pd
import os
import json
from django.http import JsonResponse
from twilio.rest import Client
import requests
from datetime import datetime
# print(current_date)
# print(current_time)
# Your Account Sid and Auth Token from twilio.com/console
# account_sid = 'ACae97bacf53365848e957abf7dfb1c048'
# auth_token = '1cd248caec171305f2068c0d4665a752'
# client = Client(account_sid, auth_token)
# print(client)
df = pd.DataFrame()
df_out_of_stock = pd.DataFrame()
df_about_to_dry = pd.DataFrame()
df_yv209d = pd.DataFrame()
df_yv208 = pd.DataFrame()
df_yv26 = pd.DataFrame()
df_yv207 = pd.DataFrame()
df_ROlist = pd.DataFrame()
df_Phone=pd.DataFrame()
df_list = []
df_out_list = []
df_list_out=[]
sheet_names = ['YV209D Pending', 'Planned', 'Invoiced', 'Yesterday Supplied','no indent']
def Dryout(data,data1,data2,data4,data3):
    data4=data4[['Rec. Code','Receiver','Mat.Code','Volume(KL)','PGI Date','InvoiceNo.']]
    data4['Rec. Code']=data4['Rec. Code'].astype('str')
    data4['Rec. Code']=data4['Rec. Code'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
    data=data[['DO NAME','RO CODE','RO NAME','PRODUCT','STATUS CRITICAL']] #'SUPPLY LOCATION','EXPECTED DRYOUT DATE/ TIME','TRANSIT TIME (HRS.)','STOCK SURVIVAL HOURS (HRS.)'
    data1=data1[['Ship2Party','Name 1','RTD(in KM)','REMARKS','Sales Document','Material']]
    data2=data2[['Material','Vehicle','Ship2Party','Name','Invoice']]
    data['PRODUCT']=data['PRODUCT'].map(lambda x:"16710" if x=='MS' else x)
    data['PRODUCT']=data['PRODUCT'].map(lambda x:"17710" if x=='XP' else x)
    data['PRODUCT']=data['PRODUCT'].map(lambda x:"50700" if x=='HSD' else x)
    data['PRODUCT']=data['PRODUCT'].map(lambda x:"17095" if x=='XP95' else x)
    data['PRODUCT']=data['PRODUCT'].astype('int')
    data['RO CODE']=data['RO CODE'].astype('str')
    data1['Ship2Party']=data1['Ship2Party'].astype('str')
    data2['Ship2Party']=data2['Ship2Party'].astype('str')
    data['RO CODE']=data['RO CODE'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
    data1['Ship2Party']=data1['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
    df_f1=pd.merge(left=data,right=data1,how='inner',left_on=['RO CODE','PRODUCT'],right_on=['Ship2Party','Material'])
    df_f1['RO CODE']=df_f1['RO CODE'].astype('str')
    data2['Ship2Party']=data2['Ship2Party'].map(lambda x:"0000"+str(x) if len(x)<=6 else x)
    df_f2=pd.merge(left=data,right=data2,how='inner',left_on=['RO CODE','PRODUCT'],right_on=['Ship2Party','Material'])
    df_con=pd.concat([df_f1[['DO NAME','RO CODE','RO NAME','PRODUCT','STATUS CRITICAL']],df_f2[['DO NAME','RO CODE','RO NAME','PRODUCT']]],ignore_index=True)
    boolen_series=data['RO CODE'].isin(df_con['RO CODE'].values.tolist())
    df_f3=data[~boolen_series]
    # writer=pd.ExcelWriter(r'\\192.168.1.39\Muniyappan\dryoutlist.xlsx',engine='xlsxwriter')
    data3['Ship2Party']=data3['Ship2Party'].map(lambda x:"0000"+str(x))
    df_f4=pd.merge(left=df_f3,right=data3,how='inner',left_on=['RO CODE'],right_on=['Ship2Party'])
    # print(".................YV209D..................")
    df_f2['Invoice']=df_f2['Invoice'].astype('str')
    df_f2['Invoice']=df_f2['Invoice'].map(lambda x:x if len(x)>4 else "Planned/UnderLoading")
    # df_f1.to_excel(writer,sheet_name="yv209d-pending")
    # print(df_f1) 
    # print(".................Planned..................")
    df_plan=df_f2[df_f2['Invoice']=="Planned/UnderLoading"]
    # df_plan.to_excel(writer,sheet_name="planned")
    # print(df_plan) 
    # print(".................Invoiced..................")
    df_invoiced=df_f2[df_f2['Invoice']!="Planned/UnderLoading"]
    # df_invoiced.to_excel(writer,sheet_name="Invoiced")
    # print(df_invoiced) 
    df_f5=pd.merge(left=df_f4,right=data4,how='inner',left_on=['RO CODE','PRODUCT'],right_on=['Rec. Code','Mat.Code'])
    # print(".................Indent supplied yesterday..................")
    # df_f5.to_excel(writer,sheet_name="Yesterday Supplied")
    # print(df_f5) 
    df_f4["ROMaterial"]=df_f4["RO CODE"].astype('str')+df_f4["PRODUCT"].astype('str')
    data4["ROMaterial"]=data4["Rec. Code"].astype('str')+data4["Mat.Code"].astype('str')
    boolen_yv26=df_f4['ROMaterial'].isin(data4['ROMaterial'].values.tolist())
    df_f4=df_f4[~boolen_yv26]
    # print(".................Indent Not Placed..................")
    # df_f4.to_excel(writer,sheet_name="no indent")
    # print(df_f4) 
    # writer.save()
    data1=data1[['Ship2Party','Name 1','RTD(in KM)','REMARKS','Sales Document','Material']]
    Ship2Party=df_f1['Ship2Party'].values.tolist()
    CustomerName=df_f1['Name 1'].values.tolist()
    SalesDocument=df_f1['Sales Document'].values.tolist()
    Remarks=df_f1['REMARKS'].values.tolist()
    # for remark in Remarks:
    #     if len(remark)>5:
    #         # Massage_body= "Dear, "+CustomerName[Remarks.index(remark)]+"-"+Ship2Party[Remarks.index(remark)]+"SO Number: " +SalesDocument[Remarks.index(remark)] +"cannot be executed due to :" +remark
    #         Massage_body= "Dear, {0} ({1}) SO Number: {2} cannot be executed due to : {3}"\
    #         .format(CustomerName[Remarks.index(remark)],Ship2Party[Remarks.index(remark)],+SalesDocument[Remarks.index(remark)],remark)
    #         message = client.messages.create(
    #                         body=Massage_body,
    #                         from_='+13344543826',
    #                         to='+918870887201'
    #                     )
    #         print(message.sid)
    return [df_f1,df_plan,df_invoiced,df_f5,df_f4]
def index(request):
        print("is_authenticated",request.user.is_authenticated)
    # if request.user.is_authenticated:
        now=datetime.now()
        current_date=now.strftime("%d-%m-%Y")
        current_time=now.strftime("%H%M")
        global sap_density_list, tas_density_list,df,df_out_of_stock,df_about_to_dry,df_yv209d,df_yv208,df_yv26,df_yv207,df_list,df_ROlist,\
        df_out_list,df_list_out,df_Phone
        print(request.POST)
        if "GET" == request.method:
            return render(request, 'index.html')
        else:
            if 'dryout' in request.FILES:
                # Here it is already not empty, and you can attach
                excel_file1 = request.FILES.getlist('dryout')
                for i in excel_file1:
                    print(i)
                    if str(i).lower().endswith('.csv'):
                        df = pd.read_csv(i, index_col=False)
                    elif str(i).lower().endswith(('.xls', '.xlsx')):
                        sheets=pd.read_excel(i,sheet_name=None)
                        df = pd.concat(sheets[frame] for frame in sheets.keys())
                    df_list.append(df)
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
                        df_out_of_stock = df_out_of_stock[
                            ['SO NAME', 'DO NAME', 'SALES AREA', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS CRITICAL',
                             'RO-PRODUCT']]
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
                             'RO-PRODUCT']]
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
                df_dryout_in = pd.concat([df_about_to_dry, df_out_of_stock], ignore_index=True)
                df_out_list.append(df_dryout_in)
                df_out_list.append(df_out_of_stock)
                df_out_list.append(df_about_to_dry)
                df_list_out=Dryout(df_dryout_in,df_yv209d,df_yv208,df_yv26,df_ROlist).copy()
                select=["YV209D-dryout",'Planned','Invoiced','Yesterday Supplied','No indent','YV209D','YV208']
                if  'select' in request.POST:
                    selected_list = request.POST.get('select')
                    # add phone number
                    if selected_list=="YV209D-dryout":
                        df_f1=pd.merge(left=df_list_out[select.index(selected_list)],right=df_Phone,how='inner',left_on=['RO CODE'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'yv209d-dry.html',arg)
                    elif selected_list=="Planned":
                        df_f1=pd.merge(left=df_list_out[select.index(selected_list)],right=df_Phone,how='inner',left_on=['RO CODE'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'planned.html',arg)
                    elif selected_list=="No indent":
                        df_f1=pd.merge(left=df_list_out[select.index(selected_list)],right=df_Phone,how='inner',left_on=['RO CODE'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'noIndent.html',arg)
                    elif selected_list=="Invoiced":
                        df_f1=pd.merge(left=df_list_out[select.index(selected_list)],right=df_Phone,how='inner',left_on=['RO CODE'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'invoiced.html',arg)
                    elif selected_list=="Yesterday Supplied":
                        df_f1=pd.merge(left=df_list_out[select.index(selected_list)],right=df_Phone,how='inner',left_on=['RO CODE'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'yesterday_supplied.html',arg)
                    elif selected_list=="YV209D":
                        df_f1=pd.merge(left=df_yv209d,right=df_Phone,how='inner',left_on=['Ship2Party'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'yv209d.html',arg)
                    elif selected_list=="YV208":
                        df_f1=pd.merge(left=df_yv208,right=df_Phone,how='inner',left_on=['Ship2Party'],right_on=['Ship-To Party'])
                        print(df_f1.columns)
                        datalist=[]
                        arg={"header":df_f1.columns,"data":df_f1.values.tolist()}
                        return render(request, 'yv208.html',arg)
                # with BytesIO() as b:
                #     writer = pd.ExcelWriter(b, engine='xlsxwriter')
                #     for i, df_excel in enumerate(df_list_out):
                #         df_excel.to_excel(writer, sheet_name=sheet_names[i], index=False)
                #         # Indicate workbook and worksheet for formatting
                #         workbook = writer.book
                #         worksheet = writer.sheets[sheet_names[i]]
                #         formater = workbook.add_format({'border': 1})
                #         # Iterate through each column and set the width == the max length in that column. A padding length of 2
                #         # is also added.
                #         for j, col in enumerate(df_excel.columns):
                #             # find length of column i
                #             column_len = df_excel[col].astype(str).str.len().max()
                #             # Setting the length if the column header is larger
                #             # than the max column value length
                #             column_len = max(column_len, len(col)) + 1
                #             # set the column length
                #             worksheet.set_column(j, j, column_len, formater)
                #     writer.save()
                #     # response = HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')
                #     # response['Content-Disposition'] = 'attachment; filename="dryout status at {0} hrs on {1}.xlsx"'.format(current_time,current_date)
                #     # return response
                # return render(request, 'yv209d.html',arg)
    # else:
    #     messages.info(request, 'Please login first..')
    #     return redirect("/")

def Muni(request):
    print(request.POST)
    global df_list_out
    if  'RoName' in request.POST:
        RoName = request.POST.get('RoName')
        SO = request.POST.get('SO')
        remark = request.POST.get('remark')
        MobileNumber = request.POST.get('MobileNumber')
        print("MobileNumber",MobileNumber)
        # MobileNumber=917093890777
        print(MobileNumber)
        ### SMS #################
        mobileno=[]
        message = "Dear {0}, Your SO no:{1} cannot be processed due to {2}. More information visit {3}. IOCL SALEM Terminal- MUNIYAPPAN".format(RoName,SO,remark,'www.ioclsalem.com')
        mobileno.append('{0}'.format(MobileNumber))
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

# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect("/index")
#         else:
#             messages.info(request,'invalid credentials')
#             return render(request,'login.html')
#     else:
#         return render(request,'login.html')
# def logout(request):
#     auth.logout(request)
#     return redirect("/")