from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Employee
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.
# This Class Will Add new Item and Show All Items
class EmployeeAddShowView(TemplateView):
  template_name = 'framework/addandshow.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = StudentRegistration()
    stud = Employee.objects.all()
    context = {'stu':stud, 'form':fm}
    return context
  
  def post(self, request):
    fm = StudentRegistration(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg = Employee(name=nm, email=em, password=pw)
      reg.save()
    return HttpResponseRedirect('/')

# This Class will Update/Edit
class EmployeeUpdateView(View):
  def get(self, request, id):
    pi = Employee.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)
    return render(request, 'framework/updatestudent.html', {'form':fm})
  
  def post(self, request, id):
    pi = Employee.objects.get(pk=id)
    fm = StudentRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    return render(request, 'framework/updatestudent.html', {'form':fm})

# This Class will Delete
class EmployeeDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    Employee.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)
