from rest_framework import serializers, fields
from .models import godryModel,outofstockModel,romobileModel,rolistModel,yv26Model,yv208Model,yv209dModel
class godryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=godryModel
        fields = '__all__'
class outofstockModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=outofstockModel
        fields = '__all__'

class romobileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=romobileModel
        fields = '__all__'
class rolistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=rolistModel
        fields = '__all__'
class yv26ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=yv26Model
        fields = '__all__'

class yv208ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=yv208Model
        fields = '__all__'
class yv209dModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=yv209dModel
        fields = '__all__'