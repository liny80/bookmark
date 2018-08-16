from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# 데이터베이스와 연결하기 위한 모델을 만드는 공간
# 모델은 class 로 설계

# 백엔드 입장
# 필드이름 = 컬럼이름
# 필드종류 = 컬럼 데이터 타입
# 필드인수 = 컬럼 제약사항

# 프론트 입장
# 필드이름 = form label
# 필드종류 = 어떤 form tag
# 필드인수  = 제약사항



class Question(models.Model): # 모든 모델은 model.Model을 상속받는다
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text