from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from django.views import View
from .models import Database1
from .forms import Form1

# Create your views here.
class Student_informations(TemplateView):
    template_name = 'school/student_info.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forms = Form1()
        dbs = Database1.objects.all()
        context = {'fm':forms, 'db': dbs }
        return context
    
    def post(self, request):
        forms = Form1(request.POST)
        if forms.is_valid():
            nm = forms.cleaned_data['name']
            rl = forms.cleaned_data['roll']
            rg = forms.cleaned_data['registration']
            dp = forms.cleaned_data['department']
            data_form = Database1(name=nm, roll=rl, registration=rg, department=dp)
            data_form.save()
        return HttpResponseRedirect('/')

class Datadelete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = (kwargs['id'])
        Database1.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
        
class Search2(ListView):
    model = Database1
    template_name = 'school/search.html'
    context_object_name = 'dat'
    def get_queryset(self):
        query = self.request.GET.get('s')
        return Database1.objects.filter(roll=query)


class UpdtV(View):
    def get(self, request, id):
        pi = Database1.objects.get(pk=id)
        fm = Form1(instance=pi)
        return render(request, 'school/update.html', {'fm':fm})

    def post(self, request, id):
        pi = Database1.objects.get(pk=id)
        fm = Form1(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')



  