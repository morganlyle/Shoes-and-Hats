# from django.shortcuts import render

# from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


# Create your views here.


class ReceiptsListView(LoginRequiredMixin, TemplateView):
    # model = Receipts
    template_name = "list.html"
