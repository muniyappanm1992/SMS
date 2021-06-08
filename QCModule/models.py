from django.db import models
from .columns import yqlabColumn,yvrokarColumn
# Create your models here.
class yqlabModel(models.Model):
    class Meta:
            db_table = 'yqlab' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    yqlabColumn0 = models.CharField(max_length=100, name=yqlabColumn[0], null=False)
    yqlabColumn1 = models.CharField(max_length=100, name=yqlabColumn[1], null=True)
    yqlabColumn2 = models.CharField(max_length=100, name=yqlabColumn[2], null=False)
    yqlabColumn3 = models.CharField(max_length=100, name=yqlabColumn[3], null=False)
    yqlabColumn4 = models.CharField(max_length=100, name=yqlabColumn[4], null=False)
    yqlabColumn5 = models.CharField(max_length=100, name=yqlabColumn[5], null=False)
    yqlabColumn6 = models.CharField(max_length=100, name=yqlabColumn[6], null=True)
    yqlabColumn7 = models.CharField(max_length=100, name=yqlabColumn[7], null=True)
    yqlabColumn8 = models.CharField(max_length=100, name=yqlabColumn[8], null=False)
    yqlabColumn9 = models.CharField(max_length=100, name=yqlabColumn[9], null=True)
    yqlabColumn10 = models.CharField(max_length=100, name=yqlabColumn[10], null=True)
    yqlabColumn11 = models.CharField(max_length=100, name=yqlabColumn[11], null=True)
    yqlabColumn12 = models.CharField(max_length=100, name=yqlabColumn[12], null=True)
    yqlabColumn13 = models.CharField(max_length=100, name=yqlabColumn[13], null=True)
    yqlabColumn14 = models.CharField(max_length=100, name=yqlabColumn[14], null=True)
    yqlabColumn15 = models.CharField(max_length=100, name=yqlabColumn[15], null=True)
    yqlabColumn16 = models.CharField(max_length=100, name=yqlabColumn[16], null=True)
    yqlabColumn17 = models.CharField(max_length=100, name=yqlabColumn[17], null=True)
    yqlabColumn18 = models.CharField(max_length=100, name=yqlabColumn[18], null=True)
    yqlabColumn19 = models.CharField(max_length=100, name=yqlabColumn[19], null=True)
    yqlabColumn20 = models.CharField(max_length=100, name=yqlabColumn[20], null=True)
    yqlabColumn21 = models.CharField(max_length=100, name=yqlabColumn[21], null=True)
    yqlabColumn22 = models.CharField(max_length=100, name=yqlabColumn[22], null=True)

class yvrokarModel(models.Model):
    class Meta:
            db_table = 'yvrokar' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    yvrokarColumn0 = models.CharField(max_length=100, name=yvrokarColumn[0], null=False)
    yvrokarColumn1 = models.CharField(max_length=100, name=yvrokarColumn[1], null=True)
    yvrokarColumn2 = models.CharField(max_length=100, name=yvrokarColumn[2], null=False)
    yvrokarColumn3 = models.CharField(max_length=100, name=yvrokarColumn[3], null=True)
    yvrokarColumn4 = models.CharField(max_length=100, name=yvrokarColumn[4], null=True)
    yvrokarColumn5 = models.CharField(max_length=100, name=yvrokarColumn[5], null=True)
    yvrokarColumn6 = models.CharField(max_length=100, name=yvrokarColumn[6], null=True)
    yvrokarColumn7 = models.CharField(max_length=100, name=yvrokarColumn[7], null=True)
    yvrokarColumn8 = models.CharField(max_length=100, name=yvrokarColumn[8], null=True)
    yvrokarColumn9 = models.CharField(max_length=100, name=yvrokarColumn[9], null=True)
    yvrokarColumn10 = models.CharField(max_length=100, name=yvrokarColumn[10], null=True)
    yvrokarColumn11 = models.CharField(max_length=100, name=yvrokarColumn[11], null=True)
    yvrokarColumn12 = models.CharField(max_length=100, name=yvrokarColumn[12], null=True)
    yvrokarColumn13 = models.CharField(max_length=100, name=yvrokarColumn[13], null=True)
    yvrokarColumn14 = models.CharField(max_length=100, name=yvrokarColumn[14], null=True)
    yvrokarColumn15 = models.CharField(max_length=100, name=yvrokarColumn[15], null=True)
    yvrokarColumn16 = models.CharField(max_length=100, name=yvrokarColumn[16], null=True)
    yvrokarColumn17 = models.CharField(max_length=100, name=yvrokarColumn[17], null=True)
    yvrokarColumn18 = models.CharField(max_length=100, name=yvrokarColumn[18], null=True)


Models=[yqlabModel,yvrokarModel]
