from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobDeleteView,
    JobUpdateView
)

urlpatterns = [
    path("", JobListView.as_view(), name="job-list"),
    path("create/", JobCreateView.as_view(), name="job-create"),
    path("detail/<pk>", JobDetailView.as_view(), name="job-detail"),
    path("update/<pk>", JobUpdateView.as_view(), name="job-update"),
    path("delete/<pk>", JobDeleteView.as_view(), name="job-delete"),

]
