from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from studentorg.models import Organization, UserProfile
from studentorg.forms import OrganizationForm, UserProfileForm
from .models import OrgMember
from .forms import OrgMemberForm
from .models import Student
from .forms import StudentForm
from .models import College, Program
from .forms import CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class ProfileView(LoginRequiredMixin, FormView):
    template_name = "profile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')
    login_url = '/accounts/login/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = UserProfile.objects.get_or_create(user=self.request.user)[0]
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]

def get_queryset(self):
    qs = super().get_queryset()
    query = self.request.GET.get('q')

    if query:
        qs = qs.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
                )
        return qs
    
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["total_students"] = Student.objects.count()

    today = timezone.now().date()
    count = (
        OrgMember.objects.filter(
            date_joined__year=today.year
        )
        .values("student")
        .distinct()
        .count()
    )

    context["students_joined_this_year"] = count
    return context

def get_ordering(self):
    allowed = ["prog_name", "college__college_name"]
    sort_by = self.request.GET.get("sort_by")
    if sort_by in allowed:
        return sort_by
    return "prog_name"

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

class StudentList(ListView):
    model = Student
    template_name = 'orgstudent_list.html'
    context_object_name = 'students'
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'orgstudent_form.html'
    success_url = reverse_lazy("student-list")

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'orgstudent_form.html'
    success_url = reverse_lazy("student-list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "orgstudent_del.html"
    success_url = reverse_lazy("student-list")

# =======================
# COLLEGE CRUD
# =======================

class CollegeList(ListView):
    model = College
    context_object_name = "colleges"
    template_name = "college_list.html"
    paginate_by = 5

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")

class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")


# =======================
# PROGRAM CRUD
# =======================

class ProgramList(ListView):
    model = Program
    context_object_name = "programs"
    template_name = "program_list.html"
    paginate_by = 5

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy("program-list")
