"""my_first_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # http://127.0.0.1:8000/admin/...
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/blog/...
    path('blog/', include('blog.urls')),
    # http://127.0.0.1:8000/webtoon/...
    path('webtoon/', include('cartoon.urls')),
    path('carrot/', include('news.urls'))

]

# 1. webtoon/로 접속하면 웹툰 메인 페이지가 나오게 해보세요
# 1-1. webtoon/dooly로 접속하면 둘리 페이지가 나오게 해보세요
# 1-2. webtoon/pororo 로 접속하면 뽀로로 페이지가 나오게 해보세요

# 2. carrot/로 접속하면 뉴스 메인 페이지가 나오게 해보세요
# 2-1. carrot/today 로 접속하면 오늘의 뉴스 페이지가 나오게 해보세요