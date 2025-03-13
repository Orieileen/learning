from django.db import models
from account.models import User
# Create your models here.
class Article(models.Model):
  id = models.IntegerField(primary_key=True)
  title = models.CharField('标题', max_length=100)
  content = models.TextField('内容')
  publish_date = models.DateTimeField('出版日期')
  user = models.ForeignKey(User, on_delete=models.CASCADE)