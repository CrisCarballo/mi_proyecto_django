from rest_framework import serializers
from new_app.models import Employee

# serializer de empleados
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el serializer