from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render(request, "index.html", { 'current_time': current_time })