from django.urls import path
from . import views

urlpatterns = [
    #
    path('', views.index),
    # add
    path('add', views.add),
    # pizza
    path('pizza',views.pizza),
    path('jazz',views.jazz),
    # path()의 세 번째 파라미터 이름은 리다이렉트 또는 링크에 사용되는 뷰의 이름이다.
    path('pizza/employees', views.employee_list, name='pizzaEmpList'),
    path('pizza/employee/add', views.employee_add, name='pizzaEmpAdd'),
    path('pizza/employee/create', views.employee_create, name='pizzaEmpCreate'),
    path('pizza/employee/delete', views.employee_delete, name='pizzaEmpDelete')
]