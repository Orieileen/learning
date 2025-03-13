from django.db import models

# Create your models here.
class User(models.Model):
  id = models.IntegerField('用户id',primary_key=True)
  username = models.CharField('用户名', max_length=10, null=True, blank=True)
  password = models.CharField('密码', max_length= 18)
  email = models.EmailField('邮箱')