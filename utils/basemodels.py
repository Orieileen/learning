from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, editable=True)

    class Meta:
      abstract = True
