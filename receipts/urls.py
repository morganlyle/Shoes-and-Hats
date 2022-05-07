from django.urls import path
from receipts.views import (
    AccountsCreateView,
    AccountsListView,
    ExpenseCategoryCreateView,
    ExpenseCategoryListView,
    ReceiptsCreateView,
    ReceiptsListView,
)

urlpatterns = [
    path("", ReceiptsListView.as_view(), name="home"),
    path("create/", ReceiptsCreateView.as_view(), name="create"),
    path(
        "accounts/create", AccountsCreateView.as_view(), name="accounts/create"
    ),
    path("accounts/", AccountsListView.as_view(), name="accounts/list"),
    path(
        "categories/create",
        ExpenseCategoryCreateView.as_view(),
        name="categories/create",
    ),
    path(
        "categories/",
        ExpenseCategoryListView.as_view(),
        name="categories/list",
    ),
]
