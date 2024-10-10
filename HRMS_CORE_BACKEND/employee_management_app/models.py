
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EMPLOYEE_DATA(models.Model):
    emp_first_name = models.CharField(max_length=50)
    emp_last_name = models.CharField(max_length=20)
    emp_username = models.CharField(max_length=20)
    emp_personal_email =models.EmailField(max_length=254)
    emp_phone_number = models.BigIntegerField()
    emp_current_address  = models.CharField(max_length=256)
    emp_permanent_address = models.CharField(max_length=256)
    # emp_reporting_manager =  models.BigIntegerField()
    emp_date_of_birth = models.DateTimeField()
    # emp_designation = models.ForeignKey()
    # emp_ctc_salary = models.DecimalField()
