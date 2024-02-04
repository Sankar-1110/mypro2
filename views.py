from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Login

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['password']

        stud = Login()
        stud.username = username
        stud.password = password
        stud.save()
    return render(request, "polls/index.html")  