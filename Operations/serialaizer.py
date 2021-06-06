from rest_framework import serializers, fields
from .models import empModel
class empModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=empModel
        fields = '__all__'
