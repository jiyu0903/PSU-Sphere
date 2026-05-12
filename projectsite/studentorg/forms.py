from django.forms import ModelForm
from django import forms
from .models import OrgMember, Organization, Student, College, Program, UserProfile

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'college', 'description']

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'lastname', 'firstname', 'middlename', 'program']

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['prog_name', 'college']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone', 'bio', 'avatar']
    class Meta:
        model = Organization
        fields = "__all__"

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"