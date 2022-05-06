# from django.shortcuts import render

# from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from receipts.models import Account, Receipts


# Create your views here.


class ReceiptsCreateView(LoginRequiredMixin, CreateView):
    model = Receipts
    template_name = "list.html"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.user_property = self.request.user
        item.save()
        return redirect("")


class AccountsCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/create.html"


class ReceiptsListView(LoginRequiredMixin, ListView):
    model = Receipts
    template_name = "receipts/list.html"
