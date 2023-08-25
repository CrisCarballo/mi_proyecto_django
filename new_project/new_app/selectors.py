from new_app.models import Employee
from typing import Iterable

# devuelve todos los empleados
def get_all_employees() -> Iterable[Employee]:
  return Employee.objects.all()

# devuelve un empleado por su id
def get_employee_by_id(id_employee: int) -> Employee:
  return Employee.objects.get(id=id_employee)