from django.contrib import admin

# Register your models here.
# 관리자 페이지에 내가 원하는 모델과 기능을 추가하기 위한 파일
from .models import *

admin.site.register(Question)