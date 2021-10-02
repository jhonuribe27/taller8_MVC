from django.shortcuts import render,HttpResponse

class indexController():
    def index(request, year):
        return HttpResponse('<h1>Juan Camilo</h1>%s' % year)