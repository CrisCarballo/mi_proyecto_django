from rest_framework.views import APIView
from rest_framework.response import Response
from new_app.serializers import EmployeeSerializer
from new_app.selectors import get_all_employees, get_employee_by_id
from new_app.services import create_employee
from rest_framework import serializers

# Create your views here.


# hola mundo
class HelloWorldAPI(APIView):

    def get(self, request):
        return Response({
            "Hola" : "Mundo"
        })


# devuelve todos los empleados
class AllEmployeesAPI(APIView):

    def get(self, request):
        return Response(
            EmployeeSerializer(get_all_employees(), many=True).data
        )
    

# devuelve un empleado
class GetEmployeeAPI(APIView):

    def get(self, request, id):
        return Response(
            EmployeeSerializer(get_employee_by_id(id)).data
        )


# crea un empleado nuevo
class CreateEmployeeAPI(APIView):
    class InputSerializer(serializers.Serializer):
        first_name=serializers.CharField(),
        last_name=serializers.CharField(),
        age=serializers.IntegerField(),
        hire_date=serializers.DateField(),
        is_admin=serializers.BooleanField(),
        salary=serializers.FloatField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print(serializer.validated_data)
        return Response(
            
            EmployeeSerializer(create_employee(**serializer.validated_data)).data
        )
