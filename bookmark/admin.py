from django.contrib import admin

# Register your models here.

from .models import Bookmark
# 어드민에서 보이게 하려면 여기서 등록해 줘야 한다.
# 즉, 어드민이라고 해도 여기서 보이게 하던가 안보이게 하던가 할 수 있는 권한이 있는 것이다.
admin.site.register(Bookmark)