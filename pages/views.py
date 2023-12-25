from django.shortcuts import render, redirect
from pages.models import *
from pages.forms import *

def home_page_view(request):
    scrolls = MainScrollModel.objects.all().order_by('-pk')
    scrolls_table = MainScrollTable.objects.all().order_by('-pk')
    context = {
        'scrolls': scrolls,
        'scrolls_table': scrolls_table
    }
    return render(request, template_name='index.html', context = context)


def reserve_view(request):
    if request.method == "POST":
       form = ReservationForm(data = request.POST)
       if form.is_valid():
           form.save()
           return redirect('pages:home')
       else:
           return render(request, template_name='index.html')
    else:
        return render(request, template_name='index.html')   
        
       