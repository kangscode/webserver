from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee,Departments

# Create your views here.

def index(request):
    context = {
        'color': 'red',
        'name': '홍길동',
        'qty': 7,
        'stock': ['규동', '돈부리', '카라아게동', '치즈돈부리', '김치치즈규동'],
    }
    return render(request, 'blog/index.html', context)
    # return HttpResponse('<html><head></head><body><h1>블로그 메인페이지 입니다</h1></body></html>')

def add(request):
    return HttpResponse('<h3>새로운 글을 등록하는 페이지입니다</h3>')

def pizza(request):
    html = '<h1>피자 주문을 받았습니다.</h1>'

    name = request.GET['name']
    topping = request.GET['topping']
    sauce = request.GET['sauce']
    # checkbox 또는 select는 여러개 넘어올 수도 있기 때문에 리스트 형태로 받아야 한다.
    extras = request.GET.getlist('extras')
    instructions = request.GET['instructions']

    if topping == 'top1':
        topping = '슈퍼슈프림 피자'
    elif topping == 'top2':
        topping = '야채 피자'
    elif topping == 'top3':
        topping = '하와이언 피자'

    if sauce == 'sauce1':
        sauce = '토마토 소스'
    elif sauce == 'sauce2':
        sauce = '크림 소스'
    elif sauce == 'sauce3':
        sauce = '소스 없음'

    if len(extras)==0:
        extras = '없음'
    elif len(extras)==1:
        if extras[0] == 'ex1':
            extras = '치즈 추가'
        elif extras[0] == 'ex2':
            extras = '글루텐 없음'
    elif len(extras)==2:
        extras = '치즈 추가, 글루텐 없음'

    html += f'주문자: {name} <br>'
    html += f'토핑: {topping} <br>'
    html += f'소스: {sauce} <br>'
    html += f'추가: {extras} <br>'
    html += f'요청사항: {instructions} <br>'


    return HttpResponse(html)


# 숙제
#  - PizzaShop처럼 서버로 데이터와 함께 요청하는 페이지를 만들 것 (input type의 종류가 다양할 것)
#  - 서버에서 전송 결과를 확인하고, 해당 데이터를 통해 웹 페이지를 응답할 것.


def jazz(request):

    # html = '<h1>재즈 동아리 신청 완료</h1>'
    #
    #
    # name = request.GET['name']
    # major = request.GET['major']
    # level = request.GET['level']
    # instrument = request.GET.getlist('instrument')
    # study = request.GET.getlist('study')
    # question = request.GET['question']
    #
    #
    # if major == 'major1':
    #     major = '경영학부'
    # elif major == 'major2':
    #     major = '공학계열'
    # elif major == 'major3':
    #     major = '소프트웨어학과'
    # elif major == 'major4':
    #     major = '자유전공학부'
    # elif major == 'major5':
    #     major = '항공교통물류학부'
    # elif major == 'major6':
    #     major = '항공우주 및 기계공학부'
    # elif major == 'major7':
    #     major = '항공운항학과'
    # elif major == 'major8':
    #     major = '항공전자정보공학부'
    # elif major == 'major9':
    #     major = '항공재료공학과'
    #
    # if level == 'low':
    #     level = '아예 없어요'
    # elif level == 'medium':
    #     level = '조금 알아요'
    # elif level == 'high':
    #     level = '기똥차요'
    #
    #
    #
    #
    # html += f'신청자: {name} <br>'
    # html += f'학부(과): {major} <br>'
    # html += f'재즈를 접한 정도: {level} <br>'
    # html += f'다룰 수 있는 악기: {instrument} <br>'
    # html += f'배우고 싶은 악기: {study} <br>'
    # html += f'문의사항: {question} <br>'
    #
    #
    # return HttpResponse(html)

    context = {
    'name' : request.GET['name'],
    'major': request.GET['major'],
    'level' : request.GET['level'],
    'instrument' : request.GET.getlist('instrument'),
    'study' : request.GET.getlist('study'),
    'question' : request.GET['question'],

    }
    return render(request, 'blog/index.html', context)



def employee_list(request):
    print(Employee.objects.all())
    print(Employee.objects.get(pk=3))

    context = {
        'employees': Employee.objects.all(),
        # 'monthly_emp': Employee.objects.get(pk=4),
        # 'lt5000': Employee.objects.filter(salary__lt=5000),
        # 'lt5000ex': Employee.objects.exclude(salary__lt=5000),
        # 'range': Employee.objects.filter(salary__range=(1000,9000)),
    }
    try:
        context['monthly_emp'] = Employee.objects.get(pk=4)
    except Employee.DoesNotExist:
        context['monthly_emp'] = Employee.objects.last()


    return render(request, 'pizza/employees.html', context)


def employee_add(request):
    context = {
        'departments': Departments.objects.all()
    }


    return render(request, 'pizza/add_employee.html', context)


def employee_create(request):
    newEmp = Employee() # Employee의 인스턴스
    newEmp.name = request.POST['name']
    newEmp.salary = request.POST['salary']
    newEmp.tel = request.POST['tel']

    # ForeignKey 필드에는 부모 타입 모델 인스턴스를 넣어야 한다.
    newEmp.dept = Departments.objects.get(pk=request.POST['dept']) # id==pk
    newEmp.save()    # 부모클래스(Model)의 기능

    # 리다이렉트 (redirect)
    #   - 접속한 사용자에게 이곳에서 만든 페이지를 보여주는 대신 다른 페이지로 보내버리는 것
    #   - 이곳에 접속한 사용자에게 내가 보내는 주소로 "다시 접속(redirect)"하도록 응답한다.
    return redirect('pizzaEmpList')

def employee_delete(request):
    goodbye_emp = Employee.objects.get(pk=request.POST['id']) # Employee의 인스턴스
    goodbye_emp.delete() # DB에 삭제 반영  # 부모클래스(Model)의 기능

    return redirect('pizzaEmpList')
    # return HttpResponse(f"<h3>\"{ goodbye_emp.name }\" 사원이 좋은 곳으로 떠났습니다.</h3>")




