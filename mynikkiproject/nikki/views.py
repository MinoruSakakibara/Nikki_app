from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Nikki


class NikkiList(ListView):
    model = Nikki
    template_name = 'nikki_list.html'
    
from django.views.generic import DetailView
from .models import Nikki


class NikkiDetail(DetailView):
    model =  Nikki
    template_name = 'nikki_detail.html'
    
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Nikki


class NikkiCreate(CreateView):
    model = Nikki
    template_name = 'nikki_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('nikki:nikki_list')