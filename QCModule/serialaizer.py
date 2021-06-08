from rest_framework import serializers, fields
from .models import yqlabModel,yvrokarModel
class yqlabModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=yqlabModel
        fields = '__all__'
class yvrokarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=yvrokarModel
        fields = '__all__'

