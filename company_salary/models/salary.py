from django.db import models

from .company import Company


class Salary(models.Model):
    employed_average = models.DecimalField(max_digits=14, decimal_places=4)
    copyright_average = models.DecimalField(max_digits=14, decimal_places=4)
    total_ssi = models.DecimalField(max_digits=14, decimal_places=4)
    date_period = models.DateTimeField(db_index=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="salaries",
        related_query_name="salary",
        db_column="company_id"
    )

    class Meta:
        db_table = 'company_salary_salaries'
