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

    
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Nikki

class NikkiUpdate(UpdateView):
    model = Nikki
    template_name = 'nikki_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('nikki:nikki_list')


from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Nikki

class NikkiDelete(DeleteView):
    model = Nikki
    template_name = 'nikki_delete.html'
    success_url = reverse_lazy('nikki:nikki_list')


class NikkiSearch(ListView):
    model = Nikki
    template_name = 'nikki_search.html'


    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__icontains=title)
        return query
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.request.GET.get('title', '')
        return context