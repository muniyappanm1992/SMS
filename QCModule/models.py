from django.db import models
from .columns import yqlabColumn,yvrokarColumn
# Create your models here.
class yqlabModel(models.Model):
    class Meta:
            db_table = 'yqlab' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    yqlabColumn0 = models.CharField(max_length=100, name=yqlabColumn[0], null=False)
    yqlabColumn1 = models.CharField(max_length=100, name=yqlabColumn[1], null=False)
    yqlabColumn2 = models.CharField(max_length=100, name=yqlabColumn[2], null=False)
    yqlabColumn3 = models.CharField(max_length=100, name=yqlabColumn[3], null=False)
    yqlabColumn4 = models.CharField(max_length=100, name=yqlabColumn[4], null=False)
    yqlabColumn5 = models.CharField(max_length=100, name=yqlabColumn[5], null=False)
    yqlabColumn6 = models.CharField(max_length=100, name=yqlabColumn[6], null=False)
    yqlabColumn7 = models.CharField(max_length=100, name=yqlabColumn[7], null=False)
    yqlabColumn8 = models.CharField(max_length=100, name=yqlabColumn[8], null=False)
    yqlabColumn9 = models.CharField(max_length=100, name=yqlabColumn[9], null=False)
    yqlabColumn10 = models.CharField(max_length=100, name=yqlabColumn[10], null=False)
    yqlabColumn11 = models.CharField(max_length=100, name=yqlabColumn[11], null=False)
    yqlabColumn12 = models.CharField(max_length=100, name=yqlabColumn[12], null=False)
    yqlabColumn13 = models.CharField(max_length=100, name=yqlabColumn[13], null=False)
    yqlabColumn14 = models.CharField(max_length=100, name=yqlabColumn[14], null=False)
    yqlabColumn15 = models.CharField(max_length=100, name=yqlabColumn[15], null=False)
    yqlabColumn16 = models.CharField(max_length=100, name=yqlabColumn[16], null=False)
    yqlabColumn17 = models.CharField(max_length=100, name=yqlabColumn[17], null=False)
    yqlabColumn18 = models.CharField(max_length=100, name=yqlabColumn[18], null=False)
    yqlabColumn19 = models.CharField(max_length=100, name=yqlabColumn[19], null=False)
    yqlabColumn20 = models.CharField(max_length=100, name=yqlabColumn[20], null=False)
    yqlabColumn21 = models.CharField(max_length=100, name=yqlabColumn[21], null=False)
    yqlabColumn22 = models.CharField(max_length=100, name=yqlabColumn[22], null=False)

class yvrokarModel(models.Model):
    class Meta:
            db_table = 'yvrokar' # This tells Django where the SQL table is
    id = models.AutoField(primary_key=True,name='id')
    yvrokarColumn0 = models.CharField(max_length=100, name=yvrokarColumn[0], null=False)
    yvrokarColumn1 = models.CharField(max_length=100, name=yvrokarColumn[1], null=False)
    yvrokarColumn2 = models.CharField(max_length=100, name=yvrokarColumn[2], null=False)
    yvrokarColumn3 = models.CharField(max_length=100, name=yvrokarColumn[3], null=False)
    yvrokarColumn4 = models.CharField(max_length=100, name=yvrokarColumn[4], null=False)
    yvrokarColumn5 = models.CharField(max_length=100, name=yvrokarColumn[5], null=False)
    yvrokarColumn6 = models.CharField(max_length=100, name=yvrokarColumn[6], null=False)
    yvrokarColumn7 = models.CharField(max_length=100, name=yvrokarColumn[7], null=False)
    yvrokarColumn8 = models.CharField(max_length=100, name=yvrokarColumn[8], null=False)
    yvrokarColumn9 = models.CharField(max_length=100, name=yvrokarColumn[9], null=False)
    yvrokarColumn10 = models.CharField(max_length=100, name=yvrokarColumn[10], null=False)
    yvrokarColumn11 = models.CharField(max_length=100, name=yvrokarColumn[11], null=False)
    yvrokarColumn12 = models.CharField(max_length=100, name=yvrokarColumn[12], null=False)
    yvrokarColumn13 = models.CharField(max_length=100, name=yvrokarColumn[13], null=False)
    yvrokarColumn14 = models.CharField(max_length=100, name=yvrokarColumn[14], null=False)
    yvrokarColumn15 = models.CharField(max_length=100, name=yvrokarColumn[15], null=False)
    yvrokarColumn16 = models.CharField(max_length=100, name=yvrokarColumn[16], null=False)
    yvrokarColumn17 = models.CharField(max_length=100, name=yvrokarColumn[17], null=False)
    yvrokarColumn18 = models.CharField(max_length=100, name=yvrokarColumn[18], null=False)


Models=[yqlabModel,yvrokarModel]
