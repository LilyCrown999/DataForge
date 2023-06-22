from rest_framework import serializers
from .models import Data


    # Data_Model = models.FilePathField()

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        