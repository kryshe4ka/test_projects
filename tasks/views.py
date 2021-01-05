from django.shortcuts import render

# Create your views here.
tasks = ["foo", "bar", "zaz"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })