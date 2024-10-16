# from django.db import models
# from django.contrib.auth.models import User
# import uuid
#
# # Role model
# class Role(models.Model):
#     role_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     role_name = models.CharField(max_length=100, verbose_name="Role Name")
#
#     def __str__(self):
#         return self.role_name
#
# # Skills model
# class Skill(models.Model):
#     skills_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     skills_name = models.CharField(max_length=100, verbose_name="Skill Name")
#
#     def __str__(self):
#         return self.skills_name  # Corrected to use skills_name
#
# # TechStack model
# class TechStack(models.Model):
#     techstack_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     techstack_name = models.CharField(max_length=100, verbose_name="Tech Stack Name")
#
#     def __str__(self):
#         return self.techstack_name
#
# # Engagement model
# class Engagement(models.Model):
#     engagement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     engagement_type = models.CharField(max_length=100, verbose_name="Engagement Type")
#
#     def __str__(self):
#         return self.engagement_type
#
# # Department model
# class Department(models.Model):
#     dept_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     dept_name = models.CharField(max_length=100, verbose_name="Department Name")
#     dept_head = models.CharField(max_length=100, verbose_name="Department Head")
#
#     def __str__(self):
#         return self.dept_name
#
# # Business Unit model
# class BusinessUnit(models.Model):
#     bu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     bu_name = models.CharField(max_length=100, verbose_name="Business Unit Name")
#
#     def __str__(self):
#         return self.bu_name
#
# # Employee model
# class EmployeeData(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#         ('N', 'Not Specified'),
#     ]
#
#     BLOOD_GROUP_CHOICES = [
#         ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
#         ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
#         ('N', 'Not Specified'),
#     ]
#
#     emp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     emp_first_name = models.CharField(max_length=50, verbose_name="First Name")
#     emp_last_name = models.CharField(max_length=20, verbose_name="Last Name")
#     emp_username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     emp_personal_email = models.EmailField(max_length=254, unique=True)
#     emp_phone_number = models.CharField(max_length=15)
#     emp_permanent_address = models.CharField(max_length=256)
#     emp_skills = models.ManyToManyField(Skill, related_name='employees')
#     emp_current_address = models.CharField(max_length=256)
#     emp_blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
#     emp_reporting_manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='reportingManager')
#     emp_tech_group = models.CharField(max_length=100)
#     emp_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
#     emp_date_of_joining = models.DateTimeField()
#     emp_dob = models.DateField()
#     emp_designation = models.CharField(max_length=100)
#     emp_years_of_experience = models.CharField(max_length=10)
#     emp_profile_photo = models.BinaryField(null=True, blank=True)
#     emp_ctc_salary = models.DecimalField(max_digits=10, decimal_places=2)
#     emp_tech_stacks = models.ManyToManyField(TechStack, related_name='employees')
#     emp_job_location = models.CharField(max_length=100)
#     emp_base_location = models.CharField(max_length=100)
#     emp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     emp_allocation_status = models.CharField(max_length=100)
#     emp_business_unit = models.ForeignKey(BusinessUnit, on_delete=models.SET_NULL, null=True)
#     emp_type_of_engagement = models.ForeignKey(Engagement, on_delete=models.SET_NULL, null=True)
#     emp_location_hr = models.CharField(max_length=100)
#
#     def save(self, *args, **kwargs):
#         # Generate username from first three letters of first name and last name
#         first_part = self.emp_first_name[:3].lower()
#         last_part = self.emp_last_name[:3].lower()
#         username_base = f"{first_part}{last_part}"
#
#         # Ensure uniqueness
#         count = 1
#         username = username_base
#         while User.objects.filter(username=username).exists():
#             username = f"{username_base}{count}"
#             count += 1
#
#         # Create User instance
#         if not self.emp_username:
#             user = User(username=username)
#             user.set_unusable_password()  # or set a random password if needed
#             user.save()
#             self.emp_username = user
#
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return f"{self.emp_first_name} {self.emp_last_name}"
#
#
# # Project model
# class Project(models.Model):
#     proj_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     proj_name = models.CharField(max_length=100, verbose_name="Project Name")
#     proj_requirement = models.TextField(verbose_name="Project Requirement")
#     proj_lead = models.CharField(max_length=100, verbose_name="Project Lead")
#     proj_manager = models.CharField(max_length=100, verbose_name="Project Manager")
#     proj_tech_stack = models.CharField(max_length=100, verbose_name="Project Tech Stack")
#     proj_status = models.CharField(max_length=100, verbose_name="Project Status")
#     proj_client_details = models.TextField(verbose_name="Client Details")
#     proj_estimate_date = models.DateTimeField()
#     proj_start_date = models.DateTimeField()
#     proj_end_date = models.DateTimeField()
#     proj_created = models.DateTimeField(auto_now_add=True)
#     proj_updated = models.DateTimeField(auto_now=True)
#     proj_business_unit = models.ForeignKey(BusinessUnit, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.proj_name
#
# # Employee and Project allocation model
# class EmployeeAndProject(models.Model):
#     employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     type_of_engagement = models.ForeignKey(Engagement, on_delete=models.SET_NULL, null=True)
#     percentage_allocation = models.FloatField()
#     role = models.CharField(max_length=100)
#     allocation_date = models.DateTimeField()
#     deallocation_date = models.DateTimeField(null=True, blank=True)
#
# # Relation tables
# class EmployeeRoleRelation(models.Model):
#     employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#
# class EmployeeTechStackRelation(models.Model):
#     employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
#     tech_stack = models.ForeignKey(TechStack, on_delete=models.CASCADE)
#
# class EmployeeSkillRelation(models.Model):
#     employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
#
# class EmployeeProjectRelation(models.Model):
#     employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     engagement = models.ForeignKey(Engagement, on_delete=models.CASCADE)
#     engagement_percentage = models.FloatField()
