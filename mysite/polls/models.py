from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# 1. models.py 변경하기
# 2. makemigrations 를 통해 변경사항에 대한 마이그레이션을 만들기
# 3. migrate 를 통해 변경사항을 데이터베이스에 적용하기
