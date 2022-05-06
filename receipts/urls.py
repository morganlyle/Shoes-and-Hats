from django.urls import path
from receipts.views import ReceiptsListView

urlpatterns = [path("", ReceiptsListView.as_view(), name="home")]
