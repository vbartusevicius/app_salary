from django.db import models

from .company import Company


class EmployeeInfo(models.Model):
    count = models.IntegerField()
    date_period = models.DateTimeField(db_index=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="employeeInfo",
        related_query_name="employeeInfo",
        db_column="company_id"
    )

    class Meta:
        db_table = 'company_salary_employee_info'
