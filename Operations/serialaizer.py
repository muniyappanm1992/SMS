from rest_framework import fields, serializers

from .models import (empModel, godryModel, outofstockModel, rolistModel,
                     romobileModel, yv26Model, yv208Model, yv209dModel,
                     yvr204qModel)


class empModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=empModel
        fields = '__all__'
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
class yvr204qModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=yvr204qModel
        fields = '__all__'

