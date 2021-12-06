from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import SnackModel


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = SnackModel

class SnackDetailListView(DetailView):
    template_name = 'snack_detail.html'
    model = SnackModel
