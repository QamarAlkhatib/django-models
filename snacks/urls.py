from django.urls import path
from .views import SnackListView,SnackDetailListView

urlpatterns = [
    path('',SnackListView.as_view(), name="snack_list"),
    path("<int:pk>", SnackDetailListView.as_view(), name="snack_detail")
]