from django.shortcuts import render
from pages.models import *

def home_page_view(request):
    scrolls = MainScrollModel.objects.all().order_by('-pk')
    scrolls_table = MainScrollTable.objects.all().order_by('-pk')
    context = {
        'scrolls': scrolls,
        'scrolls_table': scrolls_table
    }
    return render(request, template_name='index.html', context = context)