from django.db import models
from django.contrib.auth.models import User
import uuid

class EmployeeData(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Not Specified'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
        ('N', 'Not Specified'),
    ]

    emp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emp_first_name = models.CharField(max_length=50, verbose_name="First Name")
    emp_last_name = models.CharField(max_length=20, verbose_name="Last Name")
    emp_username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    emp_personal_email = models.EmailField(max_length=254, unique=True)
    emp_phone_number = models.CharField(max_length=15)
    emp_permanent_address = models.CharField(max_length=256)
    emp_skills = models.ManyToManyField('Skill', related_name='employees')
    emp_current_address = models.CharField(max_length=256)
    emp_blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    emp_reporting_manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='reportingManager')
    emp_tech_group = models.CharField(max_length=100)
    emp_department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    emp_date_of_joining = models.DateTimeField()
    emp_dob = models.DateField()
    emp_designation = models.CharField(max_length=100)
    emp_years_of_experience = models.CharField(max_length=10)
    emp_profile_photo = models.BinaryField(null=True, blank=True)
    emp_ctc_salary = models.DecimalField(max_digits=10, decimal_places=2)
    emp_tech_stacks = models.ManyToManyField('TechStack', related_name='employees')
    emp_job_location = models.CharField(max_length=100)
    emp_base_location = models.CharField(max_length=100)
    emp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    emp_allocation_status = models.CharField(max_length=100)
    emp_business_unit = models.ForeignKey('BusinessUnit', on_delete=models.SET_NULL, null=True)
    emp_type_of_engagement = models.ForeignKey('Engagement', on_delete=models.SET_NULL, null=True)
    emp_location_hr = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        first_part = self.emp_first_name[:3].lower()
        last_part = self.emp_last_name[:3].lower()
        username_base = f"{first_part}{last_part}"

        count = 1
        username = username_base
        while User.objects.filter(username=username).exists():
            username = f"{username_base}{count}"
            count += 1

        if not self.emp_username:
            user = User(username=username)
            user.set_unusable_password()
            user.save()
            self.emp_username = user

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.emp_first_name} {self.emp_last_name}"
