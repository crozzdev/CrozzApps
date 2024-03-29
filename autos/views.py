from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)
    
class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)
    

# Auto CRUD OPERATIONS VIEWS

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


# Make CRUD OPERATIONS VIEWS

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")