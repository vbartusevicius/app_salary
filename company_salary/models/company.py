from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'company_salary_companies'
