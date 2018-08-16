from django.db import models

# Create your models here.


class Bookmark(models.Model):

    # 필드목적 1 : 데이터베이스 컬럼을 결정
    # 필드목적 2 : 프론트에서 어떤 form tag와 제약조건을 설정할것인지

    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name + " : " + self.url

    class Meta:
        # 메타 클래스 : 해당 모델에 대한 옵션값을 넣는다
        # 정렬, 출력될 모델 이름
        ordering = ['site_name']


    # Todo : get_absolute_url
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bookmark:detail', args=[str(self.id)])
