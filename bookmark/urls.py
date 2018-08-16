from django.urls import path
from . import views

# 함수형 뷰 : 함수이름만
# 클래스형 뷰 : 클래스이름.as_view()

# url 이름을 가지고 패턴을 찾고자 할 때 namespace를 사용하려면 app_name 이 필수!
app_name = 'bookmark' # 네임스페이스. 구분해 주기 위한 구분자다

urlpatterns = [
    path('', views.BookmarkListView.as_view(), name='list'),
    path('write/', views.BookmarkCreateView.as_view(), name='write'),
    path('detail/<int:pk>', views.BookmarkDetailView.as_view(), name='detail'),
    # <1:2> = 1. Data Type, 2. Data Name
    path('update/<int:pk>', views.BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookmarkDeleteView.as_view(), name='delete'),
]