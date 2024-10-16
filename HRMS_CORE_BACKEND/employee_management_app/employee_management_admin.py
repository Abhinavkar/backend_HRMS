from django.contrib import admin

from models.techstack_model import TechStack
from models.engagment_model import Engagement
from models.department_model import Department
from models.bu_model import BusinessUnit
from models.employee_model import EmployeeData
from models.skill_model import Skill
from models.role_model import Role
from models.emp_project_model import EmployeeAndProject
from models.emp_role_model import EmployeeRoleRelation
from models.emp_techstack_model import EmployeeTechStackRelation
from models.emp_skill_model import EmployeeSkillRelation


# Register your models here.
admin.site.register(Role)
admin.site.register(Skill)
admin.site.register(TechStack)
admin.site.register(Engagement)
admin.site.register(Department)
admin.site.register(BusinessUnit)
admin.site.register(EmployeeData)
admin.site.register(EmployeeAndProject)
admin.site.register(EmployeeRoleRelation)
admin.site.register(EmployeeTechStackRelation)
admin.site.register(EmployeeSkillRelation)
