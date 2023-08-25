import datetime
from new_app.models import Employee


# crea un empleado en la bd y lo devuelve
def create_employee(
        *,
        first_name: str,
        last_name: str,
        age: int,
        hire_date: datetime.date,
        is_admin: bool,
        salary: float,
        ) -> Employee:
    
    employee = Employee.objects.create(
        first_name=first_name,
        last_name=last_name,
        age=age,
        hire_date=hire_date,
        is_admin=is_admin,
        salary=salary
    )

    return employee

'''
{
        "first_name": "nombre de empleado admin",
        "last_name": "apellido de empleado admin",
        "age": 40,
        "hire_date": "2021-12-15",
        "is_admin": true,
        "salary": "500000.00"
}
'''