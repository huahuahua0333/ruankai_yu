from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    return render(request,'user_list.html')

def user_add(request):
    return render(request,'user_add.html')

def weather(req):
    import requests
    res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=30.67&longitude=104.07&current=temperature_2m")
    print(res.json())
    return render(req,'weather.html',{"weather_list":res.json()})
# Create your views here.

def something(request):
    return redirect("https://www.baidu.com")

def tpl(request):
    name = "韩超发方法"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "郭智", "salary": 100000, 'role': "CTO"}

    data_list = [
        {"name": "郭智", "salary": 100000, 'role': "CTO"},
        {"name": "卢慧", "salary": 100000, 'role': "CTO"},
        {"name": "赵建先", "salary": 100000, 'role': "CTO"},
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, 'n3': user_info, "n4": data_list})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.chinaunicom.com.cn/")

    # return HttpResponse("登录失败")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})

from app01.models import UserInfo,Department
def orm(request):
    Department.objects.create(title="销售部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="运营部")
    UserInfo.objects.create(name="郭智",password="123",age=30)
    UserInfo.objects.create(name="卢慧",password="123",age=30)
    UserInfo.objects.create(name="赵建先",password="123")

    #

    #
    #
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()
    #
    # UserInfo.objects.all().delete()
    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id, obj.name,obj.password,obj.age)

    # date_list = UserInfo.objects.filter(id = 1)
    # print(date_list)
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)

    # UserInfo.objects.all().update(password=999)
    # UserInfo.objects.filter(id=2).update(age=999)
    # UserInfo.objects.filter(name="李白").update(age=999)
    # return HttpResponse("成功")


def info_list(request):
    data_list = UserInfo.objects.all
    return render(request,"info_list.html",
                  {"data_list":data_list})

def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    UserInfo.objects.create(name = user,password = pwd,age = age)
    return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")