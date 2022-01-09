godryColumn=['SO NAME', 'DO NAME', 'SALES AREA', 'RO CODE', 'RO NAME', 'SUPPLY LOCATION', 'PRODUCT', 'NO OF TANKS', 'TANKAGE', 'STOCK DATE/ TIME', 'STOCK AVAILABLE (L)', 'DEAD STOCK (L)', 'STOCK ON WHEEL AVAILABLE (L)', 'PENDING INDENT QUANTITY (L)', 'AVERAGE NOZZLE SALES (L)', 'INDENT EXECUTION TIME (HRS)', 'TRANSIT TIME (HRS)', 'STOCK SURVIVAL HOURS (HRS)', 'EXPECTED DRYOUT DATE/ TIME', 'STATUS']
outofstockColumn=['SO NAME', 'DO NAME', 'SALES AREA', 'DATE', 'RO CODE', 'RO NAME', 'PRODUCT', 'NO OF TANK', 'TOTAL HOURS STOCK OUT', 'POTENTIAL LOSS (IN LITERS)', 'STOCK OUT HOURS - CUR MONTH', 'POTENTIAL LOSS - CUR MONTH (IN LITERS)', 'STOCK OUT HOURS - PREVIOUS MONTH', 'POTENTIAL LOSS - PREVIOUS MONTH (IN LITERS)']
romobileColumn=['Mobile Number', 'Ship-To Party', 'Sales Office', 'Distribution Channel', 'DifferReferCode', 'Mobile Type', 'Name 1', 'City', 'Description', 'Created By', 'Created On', 'Time', 'E-Mail Address']
rolistColumn=['Ship2Party', 'Name', 'SOff', 'Rg']
yv26Column=['Rec Code', 'Receiver', 'Document', 'DispMatDoc', 'DispItem', 'DispStLoc', 'RecvMatDoc', 'RecvItem', 'RecvStLoc', 'PGI Date', 'Batch', 'MatCode', 'MoT', 'InvoiceNo', 'AssignNo', 'Volume(KL)', 'Volume(K15)', 'Volume(K29)', 'Volume(TO)', 'Qty(EA)', 'State']
yv208Column=['Exception', 'Material', 'Shipment', 'ShpStatus', 'Vehicle', 'Ship2Party', 'Name', 'Delivery', 'Quantity', 'Sales Unit', 'Delivery quantity', 'Seal No', 'Invoice']
yv209dColumn=['Exception', 'DelCt', 'PRTY', 'Requested delivdate', 'Sales Document', 'Distribution Channel', 'Ship2Party', 'Name 1', 'RTD(in KM)', 'Material', 'OrderQty', 'Target quantity UoM', 'Truck no', 'Sales Group Desc', 'REMARKS', 'Sales Document Type', 'Sales Document Item', 'Created By', 'Sales Group']
yvr204qColumn=['Plant','Vehicle Number','Transport Tender Reference','Carrier','Name','Reprt Date','Reprt Time','Remarks','Error Type','Ship-to Party of unack Invoice']

Columns=[godryColumn,outofstockColumn,romobileColumn,rolistColumn,yv26Column,yv208Column,yv209dColumn,yvr204qColumn]

yv209dDryoutColumn=['DO NAME', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS', 'RTD(in KM)', 'REMARKS','Sales Document', 'Mobile Number','Mobile Type']
plannedColumn=['DO NAME', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS','Vehicle', 'Invoice','Mobile Number','Mobile Type']
invoicedColumn=['DO NAME', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS','Vehicle', 'Invoice','Mobile Number','Mobile Type']
YesterdaySuppliedColumn=['DO NAME', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS','Volume(KL)', 'PGI Date','InvoiceNo','Mobile Number', 'Mobile Type']
NoIndentColumn=['DO NAME', 'RO CODE', 'RO NAME', 'PRODUCT', 'STATUS','Mobile Number','Mobile Type','EXPECTED DRYOUT DATE/ TIME']
YV209DColumn=['Sales Document','Sales Office','Sales Group Desc','Ship2Party','Name 1_x','Material','OrderQty', 'Mobile Number', 'Mobile Type','REMARKS','RTD(in KM)'] #,'Requested delivdate'
YV208Column=['Sales Office','Ship2Party', 'Name','Material','Quantity', 'Shipment', 'ShpStatus', 'Vehicle', 'Delivery','Invoice', 'Mobile Number', 'Mobile Type']
HTMLColumn=[yv209dDryoutColumn,plannedColumn,invoicedColumn,YesterdaySuppliedColumn,NoIndentColumn,YV209DColumn,YV208Column]
MaterialCode=['16700','16710','17700','17710','17095','50700','32000','40000']
MaterianDescription=['MS','MS','XP','XP','XP95','HSD','ATF','SKO']
dbTableName={'godry':'godry','outofstock':'outofstock','romobile':'romobile','rolist':'rolist','yv26':'yv26','yv208':'yv208','yv209d':'yv209d','yvr204q':'yvr204q'}
select=["YV209D-dryout",'Planned','Invoiced','Yesterday Supplied','No indent','YV209D','YV208']
sheet_names = ['YV209D Pending', 'Planned', 'Invoiced', 'Yesterday Supplied','no indent']

VIEWS=['FALSE_FILLING','LPTOTALIZER','TRUCKSUM','VAUDIT_REPORT','VDDITIVETOTALIZER','VETHANOL_TOTALIZER','VEVENTALARM',\
    'VEXCEPTION_REPORT','VTOTALIZER1','VTRUCKMOVEMENTSTATUS','VTRUCKMOVEMENT_MAIN',\
        'VTRUCK_HISTORY_DETAILED','VTRUCK_HISTORY_NEW','VTRUCKDETAILS','VTRUCKMOVEMENT_BASE','TT_TOPUP','TT_DENSITYTEMP','TRUCK'] #'VTRUCK_HISTORY'

Date_x=['REPORTDATE','REPORTDATE','REPORTDATE','EVENTDATE','REPORTDATE','REPORTDATE','EVENTDATE','EVENTDATE','REPORTDATE','LOADEDDATETIME',\
    'REGISTEREDDATETIME','REPORTDATE','REPORTDATE','REPORTDATE','PARKEDDATETIME','STARTTIME','TIMESTAMP','REPORTDATE']



website="www.iocsankari.in"
