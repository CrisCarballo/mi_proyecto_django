from django.urls import path
from new_app.views import CreateEmployeeAPI, HelloWorldAPI, AllEmployeesAPI, GetEmployeeAPI

urlpatterns = [
    path('hello/', HelloWorldAPI.as_view()),
    path('employee/list/', AllEmployeesAPI.as_view()),
    path('employee/<int:id>/', GetEmployeeAPI.as_view()),
    path('employee/create/', CreateEmployeeAPI.as_view())
]