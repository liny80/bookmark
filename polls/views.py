from django.shortcuts import render

# Create your views here.
# 기능과 로직을 담당하고 있음
# 함수형 뷰와 클래스형 뷰 두가지가 있음


from django.http import HttpResponse

def index(request): # 함수형 뷰는 리퀘스트 객채를 받아줌
    return HttpResponse("Hello World!")