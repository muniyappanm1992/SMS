from django.db import models

# Create your models here.
# class SAP_Density:
#     ms_density:float
#     hsd_density: float
#     sko_density: float
#     atf_density: float
# class TAS_Density:
#     ms_density:float
#     hsd_density: float
#     sko_density: float
#     atf_density: float
# class Diff_Density:
#     ms_density:float
#     hsd_density: float
#     sko_density: float
#     atf_density: float
class yv208(models.Model):
    #id=models.AutoField(primary_key=True)
    Material = models.CharField(max_length=100, null=True)
    Shipment = models.CharField(max_length=100, null=True)
    Vehicle = models.CharField(max_length=100, null=True)
    Ship2Party = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=100, null=True)
    Delivery = models.CharField(max_length=100, null=True)
    Quantity = models.CharField(max_length=100, null=True)
    Invoice = models.CharField(max_length=100, null=True)
  
