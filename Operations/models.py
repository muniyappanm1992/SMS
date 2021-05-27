from django.db import models
from .column import godryColumn,outofstockColumn,romobileColumn,rolistColumn,yv26Column,yv208Column,yv209dColumn
class godryModel(models.Model):
    class Meta:
            db_table = 'godry' # This tells Django where the SQL table is
    id=models.AutoField(primary_key=True)
    godryColumn0=models.CharField(max_length=100,name=godryColumn[0],null=True)
    godryColumn1=models.CharField(max_length=100,name=godryColumn[1],null=False)
    godryColumn2=models.CharField(max_length=100,name=godryColumn[2],null=True)
    godryColumn3=models.CharField(max_length=100,name=godryColumn[3],null=False)
    godryColumn4=models.CharField(max_length=100,name=godryColumn[4],null=False)
    godryColumn5=models.CharField(max_length=100,name=godryColumn[5],null=True)
    godryColumn6=models.CharField(max_length=100,name=godryColumn[6],null=False)
    godryColumn7=models.CharField(max_length=100,name=godryColumn[7],null=True)
    godryColumn8=models.CharField(max_length=100,name=godryColumn[8],null=True)
    godryColumn9=models.CharField(max_length=100,name=godryColumn[9],null=True)
    godryColumn10=models.CharField(max_length=100,name=godryColumn[10],null=True)
    godryColumn11=models.CharField(max_length=100,name=godryColumn[11],null=True)
    godryColumn12=models.CharField(max_length=100,name=godryColumn[12],null=True)
    godryColumn13=models.CharField(max_length=100,name=godryColumn[13],null=True)
    godryColumn14=models.CharField(max_length=100,name=godryColumn[14],null=True)
    godryColumn15=models.CharField(max_length=100,name=godryColumn[15],null=True)
    godryColumn16=models.CharField(max_length=100,name=godryColumn[16],null=True)
    godryColumn17=models.CharField(max_length=100,name=godryColumn[17],null=True)
    godryColumn18=models.CharField(max_length=100,name=godryColumn[18],null=False)
    godryColumn19=models.CharField(max_length=100,name=godryColumn[19],null=False)
class outofstockModel(models.Model):
    class Meta:
            db_table = 'outofstock' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True)
    outofstockColumn0=models.CharField(max_length=100,name=outofstockColumn[0],null=True)
    outofstockColumn1=models.CharField(max_length=100,name=outofstockColumn[1],null=False)
    outofstockColumn2=models.CharField(max_length=100,name=outofstockColumn[2],null=True)
    outofstockColumn3=models.CharField(max_length=100,name=outofstockColumn[3],null=True)
    outofstockColumn4=models.CharField(max_length=100,name=outofstockColumn[4],null=False)
    outofstockColumn5=models.CharField(max_length=100,name=outofstockColumn[5],null=False)
    outofstockColumn6=models.CharField(max_length=100,name=outofstockColumn[6],null=False)
    outofstockColumn7=models.CharField(max_length=100,name=outofstockColumn[7],null=True)
    outofstockColumn8=models.CharField(max_length=100,name=outofstockColumn[8],null=True)
    outofstockColumn9=models.CharField(max_length=100,name=outofstockColumn[9],null=True)
    outofstockColumn10=models.CharField(max_length=100,name=outofstockColumn[10],null=True)
    outofstockColumn11=models.CharField(max_length=100,name=outofstockColumn[11],null=True)
    outofstockColumn12=models.CharField(max_length=100,name=outofstockColumn[12],null=True)
    outofstockColumn13=models.CharField(max_length=100,name=outofstockColumn[13],null=True)
class romobileModel(models.Model): 
    class Meta:
            db_table = 'romobile' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True)
    romobileColumn0=models.CharField(max_length=100,name=romobileColumn[0],null=False)
    romobileColumn1=models.CharField(max_length=100,name=romobileColumn[1],null=False)
    romobileColumn2=models.CharField(max_length=100,name=romobileColumn[2],null=False)
    romobileColumn3=models.CharField(max_length=100,name=romobileColumn[3],null=True)
    romobileColumn4=models.CharField(max_length=100,name=romobileColumn[4],null=True)
    romobileColumn5=models.CharField(max_length=100,name=romobileColumn[5],null=False)
    romobileColumn6=models.CharField(max_length=100,name=romobileColumn[6],null=False)
    romobileColumn7=models.CharField(max_length=100,name=romobileColumn[7],null=True)
    romobileColumn8=models.CharField(max_length=100,name=romobileColumn[8],null=True)
    romobileColumn9=models.CharField(max_length=100,name=romobileColumn[9],null=True)
    romobileColumn10=models.CharField(max_length=100,name=romobileColumn[10],null=True)
    romobileColumn11=models.CharField(max_length=100,name=romobileColumn[11],null=True)
    romobileColumn12=models.CharField(max_length=100,name=romobileColumn[12],null=True)
class rolistModel(models.Model): 
    class Meta:
            db_table = 'rolist' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True)
    rolistColumn0=models.CharField(max_length=100,name=rolistColumn[0],null=False)
    rolistColumn1=models.CharField(max_length=100,name=rolistColumn[1],null=True)
    rolistColumn2=models.CharField(max_length=100,name=rolistColumn[2],null=True)
    rolistColumn3=models.CharField(max_length=100,name=rolistColumn[3],null=True)
class yv26Model(models.Model): 
    class Meta:
            db_table = 'yv26' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True)
    yv26Column0=models.CharField(max_length=100,name=yv26Column[0],null=False)
    yv26Column1=models.CharField(max_length=100,name=yv26Column[1],null=False)
    yv26Column2=models.CharField(max_length=100,name=yv26Column[2],null=True)
    yv26Column3=models.CharField(max_length=100,name=yv26Column[3],null=True)
    yv26Column4=models.CharField(max_length=100,name=yv26Column[4],null=True)
    yv26Column5=models.CharField(max_length=100,name=yv26Column[5],null=True)
    yv26Column6=models.CharField(max_length=100,name=yv26Column[6],null=True)
    yv26Column7=models.CharField(max_length=100,name=yv26Column[7],null=True)
    yv26Column8=models.CharField(max_length=100,name=yv26Column[8],null=True)
    yv26Column9=models.CharField(max_length=100,name=yv26Column[9],null=False)
    yv26Column10=models.CharField(max_length=100,name=yv26Column[10],null=True)
    yv26Column11=models.CharField(max_length=100,name=yv26Column[11],null=False)
    yv26Column12=models.CharField(max_length=100,name=yv26Column[12],null=True)
    yv26Column13=models.CharField(max_length=100,name=yv26Column[13],null=False)
    yv26Column14=models.CharField(max_length=100,name=yv26Column[14],null=True)
    yv26Column15=models.CharField(max_length=100,name=yv26Column[15],null=False)
    yv26Column16=models.CharField(max_length=100,name=yv26Column[16],null=True)
    yv26Column17=models.CharField(max_length=100,name=yv26Column[17],null=True)
    yv26Column18=models.CharField(max_length=100,name=yv26Column[18],null=True)
    yv26Column19=models.CharField(max_length=100,name=yv26Column[19],null=True)
    yv26Column20=models.CharField(max_length=100,name=yv26Column[20],null=True)
class yv208Model(models.Model):
    class Meta:
            db_table = 'yv208' # This tells Django where the SQL table is
    id=models.AutoField(primary_key=True)
    yv208Column0=models.CharField(max_length=100,name=yv208Column[0],null=True)
    yv208Column1=models.CharField(max_length=100,name=yv208Column[1],null=False)
    yv208Column2=models.CharField(max_length=100,name=yv208Column[2],null=True)
    yv208Column3=models.CharField(max_length=100,name=yv208Column[3],null=True)
    yv208Column4=models.CharField(max_length=100,name=yv208Column[4],null=False)
    yv208Column5=models.CharField(max_length=100,name=yv208Column[5],null=False)
    yv208Column6=models.CharField(max_length=100,name=yv208Column[6],null=False)
    yv208Column7=models.CharField(max_length=100,name=yv208Column[7],null=True)
    yv208Column8=models.CharField(max_length=100,name=yv208Column[8],null=True)
    yv208Column9=models.CharField(max_length=100,name=yv208Column[9],null=True)
    yv208Column10=models.CharField(max_length=100,name=yv208Column[10],null=True)
    yv208Column11=models.CharField(max_length=100,name=yv208Column[11],null=True)
    yv208Column12=models.CharField(max_length=100,name=yv208Column[12],null=True)
class yv209dModel(models.Model):  
    class Meta:
            db_table = 'yv209d' # This tells Django where the SQL table is
    id=models.AutoField(primary_key=True)
    yv209dColumn0=models.CharField(max_length=100,name=yv209dColumn[0],null=True)
    yv209dColumn1=models.CharField(max_length=100,name=yv209dColumn[1],null=True)
    yv209dColumn2=models.CharField(max_length=100,name=yv209dColumn[2],null=True)
    yv209dColumn3=models.CharField(max_length=100,name=yv209dColumn[3],null=True)
    yv209dColumn4=models.CharField(max_length=100,name=yv209dColumn[4],null=False)
    yv209dColumn5=models.CharField(max_length=100,name=yv209dColumn[5],null=True)
    yv209dColumn6=models.CharField(max_length=100,name=yv209dColumn[6],null=False)
    yv209dColumn7=models.CharField(max_length=100,name=yv209dColumn[7],null=False)
    yv209dColumn8=models.CharField(max_length=100,name=yv209dColumn[8],null=False)
    yv209dColumn9=models.CharField(max_length=100,name=yv209dColumn[9],null=False)
    yv209dColumn10=models.CharField(max_length=100,name=yv209dColumn[10],null=True)
    yv209dColumn11=models.CharField(max_length=100,name=yv209dColumn[11],null=True)
    yv209dColumn12=models.CharField(max_length=100,name=yv209dColumn[12],null=True)
    yv209dColumn13=models.CharField(max_length=100,name=yv209dColumn[13],null=True)
    yv209dColumn14=models.CharField(max_length=100,name=yv209dColumn[14],null=True)
    yv209dColumn15=models.CharField(max_length=100,name=yv209dColumn[15],null=True)
    yv209dColumn16=models.CharField(max_length=100,name=yv209dColumn[16],null=True)
    yv209dColumn17=models.CharField(max_length=100,name=yv209dColumn[17],null=True)
    yv209dColumn18=models.CharField(max_length=100,name=yv209dColumn[18],null=True)
Models=[godryModel,outofstockModel,romobileModel,rolistModel,yv26Model,yv208Model,yv209dModel]
# class empModel(models.Model): 
#     class Meta:
#         db_table = 'mytable' # This tells Django where the SQL table is
#         # managed = True # Use this if table already exists
#  
#     Name=models.CharField(max_length=100,null=True,name="Name")
#     Age=models.CharField(max_length=100,null=True,name="Age")