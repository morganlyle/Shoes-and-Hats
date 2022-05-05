from django.urls import path
from receipts.views import ReceiptsTemplateView

urlpatterns = [
    path("receipts/", ReceiptsTemplateView.as_view(), name="receipts")
]
