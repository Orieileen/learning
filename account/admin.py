from django.contrib import admin
from account.models import User

# 导入Django admin模块和User模型

class UserAdmin(admin.ModelAdmin):
    """
    用户管理类
    用于在Django admin后台管理用户信息
    """
    # 设置在后台admin列表页面显示的字段，例如：显示username和email，但是models.py中将这两个值赋予了verbose_name，所以实际显示为verbose_name
    list_display = ('username','email')
    # 配置过滤字段(例：根据以下字段做的筛选器)
    list_filter = ('username','email')
# 注册User模型到admin后台,使用UserAdmin类进行管理
admin.site.register(User, UserAdmin)
