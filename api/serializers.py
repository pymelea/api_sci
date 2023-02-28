from rest_framework import serializers

from .models import Environment


class EnviromentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['name', 'capacity', 'address', 'available', 'description', 'created_by',]
        
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['name', 'cpf', 'fee', 'real_value_pay', 'capacity', 'start_day', 'end_day', 'created_by', 'updated_by', 'status', 'env', ]
        







