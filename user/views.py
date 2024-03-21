from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.


def user_register(request):
    message = ""
    form = UserCreationForm()
    # 取得所有all
    # print(User.objects.all())
    # 取得唯一 get
    # print(User.objects.get(username="brad"))
    # 取得篩選 filter
    # print(User.objects.filter(username="brad"))

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username, password1, password2)

        try:
            if len(password1) < 8:
                message = "密碼至少 8 個字元"
            elif password1 != password2:
                message = "兩次密碼不匹配"
            else:
                # 檢查使用者是否存在
                user = User.objects.filter(username=username)
                if len(user) >= 1:
                    message = "帳號已存在"
                else:
                    User.objects.create_user(
                        username=username, password=password1).save()
                    message = '註冊成功'
        except Exception as e:
            print(e)
            message = "不明錯誤發生"
    return render(request, "user/register.html", {"form": form, "message": message})
