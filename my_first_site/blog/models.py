from django.db import models

# models.py
#   - 이 프로그램에서 사용할 테이블의 형태(데이터의 형태)를 정의하는 곳이다
#   - 클래스 형태로 테이블의 구조를 정의하면 Django가 그것을 기준으로 DB에 반영한다.
#   - 모델을 정의한 후에 manage.py를 통해 마이그레이션을 진행해야 한다.

#   1. python manage.py makemigrations - models.py를 참조하여 DB에 반영할 준비를 한다.
#   (반영할 쿼리문 확인하기 python manage.py sqlmigrate app_label migration_name)
#   2. python manage.py migrate - 생성된 모든 마이그레션들을 DB에 반영한다.

'''
      No  Name    Salary   Tel              DeptNO     
      1   Smith   1000     010-1234-124     10  
      2   King    1500     012-124-1234     10           
      3   Martin  2000     010-1234-1234    20        
      4   Smith   1300     010-3333-3456    20  
'''

# DB에 원하는 데이터의 형태를 정의하기 위해 프로그래머는 모델 클래스를 model.py에 적어두어야 한다.
# 이곳에 정의한 클래스가 마이그레이션 되기 위한 기능들은 모두 models.Model 클래스에 구현되어 있고
# Django를 사용하는 프로그래머들은 Model 클래스를 상속 받아 원하는 필드만 정의해주면 된다.

class Departments(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=13)
    floor = models.IntegerField()

    def __str__(self):    # 데이터 문자로 보여줄 때
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50, default='홍길동')
    salary = models.IntegerField()
    tel = models.CharField(max_length=10)
    dept = models.ForeignKey('Departments', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}/{self.salary}/{self.tel}'

# models.py에 모델을 하나 정의하고,admin.py에 등록하고, 데이터를 5개 추가 해보세요.

class Bottle(models.Model):
    name = models.CharField(max_length=20)
    volume = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'이름: {self.name}/용량: {self.volume}ml/가격: {self.price}원'