from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    # Keep the old capitalised URL working for existing links.
    path("Projects/", RedirectView.as_view(pattern_name="projects", permanent=True)),
]
