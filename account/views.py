from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    # 业务逻辑判断
    return HttpResponse('登录成功')
  return render(request,'login.html')

class RegisterView(View):
  def get(self,request):
    return render(request,'register.html')
  def post(self,request):
    username = request.POST.get('username')
    password0 = request.POST.get('password0')
    password1 = request.POST.get('password1')
    # 业务判断逻辑
    return HttpResponse(f'{username},{password0},{password1}')



