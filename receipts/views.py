# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from receipts.models import Account, ExpenseCategory, Receipts


# Create your views here.


class ReceiptsCreateView(LoginRequiredMixin, CreateView):
    model = Receipts
    template_name = "receipts/create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.purchaser = self.request.user
        item.save()
        return redirect("home")


class ReceiptsListView(LoginRequiredMixin, ListView):
    model = Receipts
    template_name = "receipts/list.html"
    context_object_name = "receipts_list"

    def get_queryset(self):
        return Receipts.objects.filter(purchaser=self.request.user)


class AccountsCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/create.html"
    fields = ["name", "number", "owner"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("accounts/list")


class AccountsListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"
    context_object_name = "accounts/list"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(CreateView, LoginRequiredMixin):
    model = ExpenseCategory
    template_name = "expense_categories/create.html"
    fields = ["name", "category"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("categories/create")


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "expense_categories/list.html"
    context_object_name = "categories_list"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(name=self.request.user)
