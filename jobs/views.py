from django.shortcuts import render
from django.views.generic import ListView
from .models import Job


class JobListView(ListView):
    model = Job
    template_name = "jobs/job-list.html"
    context_object_name = "jobs"
    queryset = Job.objects.all()
