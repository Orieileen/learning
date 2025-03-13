from django.db import models
from utils.basemodels import BaseModel


# Create your models here.
class User(BaseModel):
  id = models.AutoField('用户id',primary_key=True)
  username = models.CharField('用户名', max_length=10, null=True, blank=True)
  password = models.CharField('密码', max_length= 18)
  email = models.EmailField('邮箱')

  class Meta:
    db_table = 'user'
    verbose_name = '用户'
