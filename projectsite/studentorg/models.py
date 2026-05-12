from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class College(BaseModel):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name

class Program(BaseModel):
    prog_name = models.CharField(max_length=150)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.prog_name

class Organization(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

class OrgMember(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField()
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name