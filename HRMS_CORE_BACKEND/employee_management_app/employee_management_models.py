from django.db import models
from django.contrib.auth.models import User
import uuid

# Role model
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Role Name")

    def __str__(self):
        return self.name

# Skills model
class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Skill Name")

    def __str__(self):
        return self.name

# TechStack model
class TechStack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Tech Stack Name")

    def __str__(self):
        return self.name

# Engagement model
class Engagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100, verbose_name="Engagement Type")

    def __str__(self):
        return self.type

# Department model
class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Department Name")
    head = models.CharField(max_length=100, verbose_name="Department Head")

    def __str__(self):
        return self.name

# Business Unit model
class BusinessUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Business Unit Name")

    def __str__(self):
        return self.name

# Employee model
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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=15)
    permanent_address = models.CharField(max_length=256)
    skills = models.ManyToManyField(Skill, related_name='employees')
    current_address = models.CharField(max_length=256)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    reporting_manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='reportees')
    tech_group = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_of_joining = models.DateTimeField()
    dob = models.DateField()
    designation = models.CharField(max_length=100)
    years_of_experience = models.CharField(max_length=10)
    profile_photo = models.BinaryField(null=True, blank=True)
    ctc_salary = models.DecimalField(max_digits=10, decimal_places=2)
    tech_stacks = models.ManyToManyField(TechStack, related_name='employees')
    job_location = models.CharField(max_length=100)
    base_location = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    allocation_status = models.CharField(max_length=100)
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.SET_NULL, null=True)
    type_of_engagement = models.ForeignKey(Engagement, on_delete=models.SET_NULL, null=True)
    location_hr = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Project model
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Project Name")
    requirement = models.TextField(verbose_name="Project Requirement")
    lead = models.CharField(max_length=100, verbose_name="Project Lead")
    manager = models.CharField(max_length=100, verbose_name="Project Manager")
    tech_stack = models.CharField(max_length=100, verbose_name="Project Tech Stack")
    status = models.CharField(max_length=100, verbose_name="Project Status")
    client_details = models.TextField(verbose_name="Client Details")
    estimate_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# Employee and Project allocation model
class EmployeeAndProject(models.Model):
    employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type_of_engagement = models.ForeignKey(Engagement, on_delete=models.SET_NULL, null=True)
    percentage_allocation = models.FloatField()
    role = models.CharField(max_length=100)
    allocation_date = models.DateTimeField()
    deallocation_date = models.DateTimeField(null=True, blank=True)

# Relation tables
class EmployeeRoleRelation(models.Model):
    employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class EmployeeTechStackRelation(models.Model):
    employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
    tech_stack = models.ForeignKey(TechStack, on_delete=models.CASCADE)

class EmployeeSkillRelation(models.Model):
    employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class EmployeeProjectRelation(models.Model):
    employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    engagement = models.ForeignKey(Engagement, on_delete=models.CASCADE)
    engagement_percentage = models.FloatField()
