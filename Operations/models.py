from django.db import models

from .column import (godryColumn, outofstockColumn, rolistColumn,
                     romobileColumn, yv26Column, yv208Column, yv209dColumn,
                     yvr204qColumn)


class godryModel(models.Model):
    class Meta:
            db_table = 'godry' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    godryColumn0=models.CharField(max_length=100,name=godryColumn[0].replace(".", ""),null=True)
    godryColumn1=models.CharField(max_length=100,name=godryColumn[1].replace(".", ""),null=False)
    godryColumn2=models.CharField(max_length=100,name=godryColumn[2].replace(".", ""),null=True)
    godryColumn3=models.CharField(max_length=100,name=godryColumn[3].replace(".", ""),null=False)
    godryColumn4=models.CharField(max_length=100,name=godryColumn[4].replace(".", ""),null=False)
    godryColumn5=models.CharField(max_length=100,name=godryColumn[5].replace(".", ""),null=True)
    godryColumn6=models.CharField(max_length=100,name=godryColumn[6].replace(".", ""),null=False)
    godryColumn7=models.CharField(max_length=100,name=godryColumn[7].replace(".", ""),null=True)
    godryColumn8=models.CharField(max_length=100,name=godryColumn[8].replace(".", ""),null=True)
    godryColumn9=models.CharField(max_length=100,name=godryColumn[9].replace(".", ""),null=True)
    godryColumn10=models.CharField(max_length=100,name=godryColumn[10].replace(".", ""),null=True)
    godryColumn11=models.CharField(max_length=100,name=godryColumn[11].replace(".", ""),null=True)
    godryColumn12=models.CharField(max_length=100,name=godryColumn[12].replace(".", ""),null=True)
    godryColumn13=models.CharField(max_length=100,name=godryColumn[13].replace(".", ""),null=True)
    godryColumn14=models.CharField(max_length=100,name=godryColumn[14].replace(".", ""),null=True)
    godryColumn15=models.CharField(max_length=100,name=godryColumn[15].replace(".", ""),null=True)
    godryColumn16=models.CharField(max_length=100,name=godryColumn[16].replace(".", ""),null=True)
    godryColumn17=models.CharField(max_length=100,name=godryColumn[17].replace(".", ""),null=True)
    godryColumn18=models.DateTimeField(max_length=100,name=godryColumn[18].replace(".", ""),null=False)
    godryColumn19=models.CharField(max_length=100,name=godryColumn[19].replace(".", ""),null=False)
    def __str__(self) -> str:
        return str(self.id)
class outofstockModel(models.Model):
    class Meta:
            db_table = 'outofstock' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    outofstockColumn0=models.CharField(max_length=100,name=outofstockColumn[0].replace(".", ""),null=True)
    outofstockColumn1=models.CharField(max_length=100,name=outofstockColumn[1].replace(".", ""),null=False)
    outofstockColumn2=models.CharField(max_length=100,name=outofstockColumn[2].replace(".", ""),null=True)
    outofstockColumn3=models.CharField(max_length=100,name=outofstockColumn[3].replace(".", ""),null=True)
    outofstockColumn4=models.CharField(max_length=100,name=outofstockColumn[4].replace(".", ""),null=False)
    outofstockColumn5=models.CharField(max_length=100,name=outofstockColumn[5].replace(".", ""),null=False)
    outofstockColumn6=models.CharField(max_length=100,name=outofstockColumn[6].replace(".", ""),null=False)
    outofstockColumn7=models.CharField(max_length=100,name=outofstockColumn[7].replace(".", ""),null=True)
    outofstockColumn8=models.CharField(max_length=100,name=outofstockColumn[8].replace(".", ""),null=True)
    outofstockColumn9=models.CharField(max_length=100,name=outofstockColumn[9].replace(".", ""),null=True)
    outofstockColumn10=models.CharField(max_length=100,name=outofstockColumn[10].replace(".", ""),null=True)
    outofstockColumn11=models.CharField(max_length=100,name=outofstockColumn[11].replace(".", ""),null=True)
    outofstockColumn12=models.CharField(max_length=100,name=outofstockColumn[12].replace(".", ""),null=True)
    outofstockColumn13=models.CharField(max_length=100,name=outofstockColumn[13].replace(".", ""),null=True)
class romobileModel(models.Model):
    class Meta:
            db_table = 'romobile' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    romobileColumn0=models.CharField(max_length=100,name=romobileColumn[0].replace(".", ""),null=False)
    romobileColumn1=models.CharField(max_length=100,name=romobileColumn[1].replace(".", ""),null=False)
    romobileColumn2=models.CharField(max_length=100,name=romobileColumn[2].replace(".", ""),null=False)
    romobileColumn3=models.CharField(max_length=100,name=romobileColumn[3].replace(".", ""),null=True)
    romobileColumn4=models.CharField(max_length=100,name=romobileColumn[4].replace(".", ""),null=True)
    romobileColumn5=models.CharField(max_length=100,name=romobileColumn[5].replace(".", ""),null=False)
    romobileColumn6=models.CharField(max_length=100,name=romobileColumn[6].replace(".", ""),null=False)
    romobileColumn7=models.CharField(max_length=100,name=romobileColumn[7].replace(".", ""),null=True)
    romobileColumn8=models.CharField(max_length=100,name=romobileColumn[8].replace(".", ""),null=True)
    romobileColumn9=models.CharField(max_length=100,name=romobileColumn[9].replace(".", ""),null=True)
    romobileColumn10=models.CharField(max_length=100,name=romobileColumn[10].replace(".", ""),null=True)
    romobileColumn11=models.CharField(max_length=100,name=romobileColumn[11].replace(".", ""),null=True)
    romobileColumn12=models.CharField(max_length=100,name=romobileColumn[12].replace(".", ""),null=True)
class rolistModel(models.Model):
    class Meta:
            db_table = 'rolist' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    rolistColumn0=models.CharField(max_length=100,name=rolistColumn[0].replace(".", ""),null=False)
    rolistColumn1=models.CharField(max_length=100,name=rolistColumn[1].replace(".", ""),null=True)
    rolistColumn2=models.CharField(max_length=100,name=rolistColumn[2].replace(".", ""),null=True)
    rolistColumn3=models.CharField(max_length=100,name=rolistColumn[3].replace(".", ""),null=True)
class yv26Model(models.Model):
    class Meta:
            db_table = 'yv26' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    yv26Column0=models.CharField(max_length=100,name=yv26Column[0].replace(".", ""),null=False)
    yv26Column1=models.CharField(max_length=100,name=yv26Column[1].replace(".", ""),null=False)
    yv26Column2=models.CharField(max_length=100,name=yv26Column[2].replace(".", ""),null=True)
    yv26Column3=models.CharField(max_length=100,name=yv26Column[3].replace(".", ""),null=True)
    yv26Column4=models.CharField(max_length=100,name=yv26Column[4].replace(".", ""),null=True)
    yv26Column5=models.CharField(max_length=100,name=yv26Column[5].replace(".", ""),null=True)
    yv26Column6=models.CharField(max_length=100,name=yv26Column[6].replace(".", ""),null=True)
    yv26Column7=models.CharField(max_length=100,name=yv26Column[7].replace(".", ""),null=True)
    yv26Column8=models.CharField(max_length=100,name=yv26Column[8].replace(".", ""),null=True)
    yv26Column9=models.DateTimeField(max_length=100,name=yv26Column[9].replace(".", ""),null=False)
    yv26Column10=models.CharField(max_length=100,name=yv26Column[10].replace(".", ""),null=True)
    yv26Column11=models.CharField(max_length=100,name=yv26Column[11].replace(".", ""),null=False)
    yv26Column12=models.CharField(max_length=100,name=yv26Column[12].replace(".", ""),null=True)
    yv26Column13=models.CharField(max_length=100,name=yv26Column[13].replace(".", ""),null=False)
    yv26Column14=models.CharField(max_length=100,name=yv26Column[14].replace(".", ""),null=True)
    yv26Column15=models.CharField(max_length=100,name=yv26Column[15].replace(".", ""),null=False)
    yv26Column16=models.CharField(max_length=100,name=yv26Column[16].replace(".", ""),null=True)
    yv26Column17=models.CharField(max_length=100,name=yv26Column[17].replace(".", ""),null=True)
    yv26Column18=models.CharField(max_length=100,name=yv26Column[18].replace(".", ""),null=True)
    yv26Column19=models.CharField(max_length=100,name=yv26Column[19].replace(".", ""),null=True)
    yv26Column20=models.CharField(max_length=100,name=yv26Column[20].replace(".", ""),null=True)
class yv208Model(models.Model):
    class Meta:
            db_table = 'yv208' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    yv208Column0=models.CharField(max_length=100,name=yv208Column[0].replace(".", ""),null=True)
    yv208Column1=models.CharField(max_length=100,name=yv208Column[1].replace(".", ""),null=False)
    yv208Column2=models.CharField(max_length=100,name=yv208Column[2].replace(".", ""),null=True)
    yv208Column3=models.CharField(max_length=100,name=yv208Column[3].replace(".", ""),null=True)
    yv208Column4=models.CharField(max_length=100,name=yv208Column[4].replace(".", ""),null=False)
    yv208Column5=models.CharField(max_length=100,name=yv208Column[5].replace(".", ""),null=False)
    yv208Column6=models.CharField(max_length=100,name=yv208Column[6].replace(".", ""),null=False)
    yv208Column7=models.CharField(max_length=100,name=yv208Column[7].replace(".", ""),null=True)
    yv208Column8=models.CharField(max_length=100,name=yv208Column[8].replace(".", ""),null=True)
    yv208Column9=models.CharField(max_length=100,name=yv208Column[9].replace(".", ""),null=True)
    yv208Column10=models.CharField(max_length=100,name=yv208Column[10].replace(".", ""),null=True)
    yv208Column11=models.CharField(max_length=100,name=yv208Column[11].replace(".", ""),null=True)
    yv208Column12=models.CharField(max_length=100,name=yv208Column[12].replace(".", ""),null=True)
class yv209dModel(models.Model):
    class Meta:
            db_table = 'yv209d' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    yv209dColumn0=models.CharField(max_length=100,name=yv209dColumn[0].replace(".", ""),null=True)
    yv209dColumn1=models.CharField(max_length=100,name=yv209dColumn[1].replace(".", ""),null=True)
    yv209dColumn2=models.CharField(max_length=100,name=yv209dColumn[2].replace(".", ""),null=True)
    yv209dColumn3=models.CharField(max_length=100,name=yv209dColumn[3].replace(".", ""),null=True)
    yv209dColumn4=models.CharField(max_length=100,name=yv209dColumn[4].replace(".", ""),null=False)
    yv209dColumn5=models.CharField(max_length=100,name=yv209dColumn[5].replace(".", ""),null=True)
    yv209dColumn6=models.CharField(max_length=100,name=yv209dColumn[6].replace(".", ""),null=False)
    yv209dColumn7=models.CharField(max_length=100,name=yv209dColumn[7].replace(".", ""),null=False)
    yv209dColumn8=models.CharField(max_length=100,name=yv209dColumn[8].replace(".", ""),null=False)
    yv209dColumn9=models.CharField(max_length=100,name=yv209dColumn[9].replace(".", ""),null=False)
    yv209dColumn10=models.CharField(max_length=100,name=yv209dColumn[10].replace(".", ""),null=True)
    yv209dColumn11=models.CharField(max_length=100,name=yv209dColumn[11].replace(".", ""),null=True)
    yv209dColumn12=models.CharField(max_length=100,name=yv209dColumn[12].replace(".", ""),null=True)
    yv209dColumn13=models.CharField(max_length=100,name=yv209dColumn[13].replace(".", ""),null=True)
    yv209dColumn14=models.CharField(max_length=100,name=yv209dColumn[14].replace(".", ""),null=True)
    yv209dColumn15=models.CharField(max_length=100,name=yv209dColumn[15].replace(".", ""),null=True)
    yv209dColumn16=models.CharField(max_length=100,name=yv209dColumn[16].replace(".", ""),null=True)
    yv209dColumn17=models.CharField(max_length=100,name=yv209dColumn[17].replace(".", ""),null=True)
    yv209dColumn18=models.CharField(max_length=100,name=yv209dColumn[18].replace(".", ""),null=True)
class yvr204qModel(models.Model):
    class Meta:
            db_table = 'yvr204q' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    TimeStampColumn = models.CharField(max_length=100, name="TimeStamp", null=True)
    ModifiedBy = models.CharField(max_length=100, name="ModifiedBy", null=True)
    yvr204qColumn0=models.CharField(max_length=100,name=yvr204qColumn[0],null=True)
    yvr204qColumn1=models.CharField(max_length=100,name=yvr204qColumn[1],null=True)
    yvr204qColumn2=models.CharField(max_length=100,name=yvr204qColumn[2],null=True)
    yvr204qColumn3=models.CharField(max_length=100,name=yvr204qColumn[3],null=True)
    yvr204qColumn4=models.CharField(max_length=100,name=yvr204qColumn[4],null=True)
    yvr204qColumn5=models.CharField(max_length=100,name=yvr204qColumn[5],null=True)
    yvr204qColumn6=models.CharField(max_length=100,name=yvr204qColumn[6],null=True)
    yvr204qColumn7=models.CharField(max_length=100,name=yvr204qColumn[7],null=True)
    yvr204qColumn8=models.CharField(max_length=100,name=yvr204qColumn[8],null=True)
    yvr204qColumn9=models.CharField(max_length=100,name=yvr204qColumn[9],null=True)

Models=[godryModel,outofstockModel,romobileModel,rolistModel,yv26Model,yv208Model,yv209dModel,yvr204qModel]
class empModel(models.Model):
    class Meta:
        db_table = 'emp' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    Name=models.CharField(max_length=100,null=True,name="Name")
    Age=models.CharField(max_length=100,null=True,name="Age")

