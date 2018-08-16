from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Bookmark
# 리스트뷰 가져다 쓸꺼니깐 리스트뷰 상속
class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 랜더링할 템플릿 파일이 지정이 되어 있다.
    # bookmark/bookmark_list.html

class BookmarkCreateView(CreateView):
    model = Bookmark # 입력화면에 출력된 Form tag를 자동으로 만들어 줌
    # 원래 이름이 _form 인데 그 뒤에 다른 이름을 붙여줄때 이걸 넣어준다
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name', 'url']
    # get_absolute_url
    success_url = reverse_lazy('bookmark:list')
    
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

    # get_absolute_url
    success_url = reverse_lazy('bookmark:list')
    
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # get_absolute_url
    success_url = reverse_lazy('bookmark:list')
    
class BookmarkDetailView(DetailView):
    model = Bookmark
    fields = ['site_name', 'url']
