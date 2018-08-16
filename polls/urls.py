from django.urls import path # 어떤 주소로 접속했을때 무슨 뷰로 보여줄것인가
from .views import *


urlpatterns = [
    path('', index, name='index'), # 아무것도 없이 접속했을때, 같은 폴더 안에 있는 views 안에 있는 index 함수를 가져올껴
]