from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'cartoon/index.html')
    # return HttpResponse('<h3>웹툰 메인 페이지</h3>')

def dooly(request):
    return HttpResponse('<h3>둘리 페이지</h3>')

def pororo(request):
    return HttpResponse('<h3>뽀로로 페이지</h3><a href="http://naver.com">눌러보세요</a>')