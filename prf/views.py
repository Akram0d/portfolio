from django.shortcuts import render

from .data import EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS


def home(request):
    context = {
        "profile": PROFILE,
        "experience": EXPERIENCE,
        "skills": SKILLS,
        "education": EDUCATION,
        "featured": [p for p in PROJECTS if p["featured"]],
    }
    return render(request, "index.html", context)


def projects(request):
    return render(request, "projects.html", {"profile": PROFILE, "projects": PROJECTS})
