from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h3>뉴스 메인 페이지</h3>')

def today(request):
    return HttpResponse('<h3>오늘의 뉴스 페이지</h3>')


