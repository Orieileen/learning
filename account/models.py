from django.db import models
from utils.basemodels import BaseModel


# Create your models here.
class User(BaseModel):
  """
  用户模型类
  用于存储用户基本信息
  """
  # 用户ID,自增主键
  id = models.AutoField('用户id',primary_key=True)
  # 用户名,最大长度10个字符,允许为空
  username = models.CharField('用户名', max_length=10, null=True, blank=True)
  # 密码,最大长度18个字符
  password = models.CharField('密码', max_length= 18)
  # 邮箱地址
  email = models.EmailField('邮箱')  # '邮箱'是这个字段在Django admin后台显示的中文名称,也叫verbose_name

  class Meta:
    """
    元数据类
    """
    # 指定数据库表名
    db_table = 'user'
    # 在admin后台显示的名称
    verbose_name = '用户'
