from django.db import models
from account.models import User
from utils.basemodels import BaseModel
# Create your models here.
class Article(BaseModel):
  id = models.IntegerField(primary_key=True)
  title = models.CharField('标题', max_length=100)
  content = models.TextField('内容')
  publish_date = models.DateTimeField('出版日期')
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'article'
    verbose_name = '文章'
    ordering = ['-publish_date']

