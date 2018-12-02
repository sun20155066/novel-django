# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import auth
from django import forms  # 导入表单
from django.contrib.auth.models import User  # 导入django自带的user表
from blog.models import Article




class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密_码 ', widget=forms.PasswordInput())


class novalForm(forms.Form):
    title = forms.CharField(label='标题', max_length=30)
    content = forms.CharField(widget=forms.Textarea, label='内容')




# Django的form的作用：
# 1、生成html标签
# 2、用来做用户提交的验证
# Form的验证思路
# 前端：form表单
# 后台：创建form类，当请求到来时，先匹配，匹配出正确和错误信息。
def index(request):
    return render(request, 'index.html')


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  # 包含用户名和密码
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            password = uf.cleaned_data['password']

            if User.objects.filter(username=username):
                return render(request, 'share1.html', { 'username': username})
            else:
                # 添加到数据库
                User.objects.create_user(username=username, password=password)
                return redirect('/login/')  # 跳转--redirect指从一个旧的url转到一个新的url


    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request, 'regist1.html', {'uf': uf})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print
        username, password
        re = auth.authenticate(username=username, password=password)  # 用户认证
        if re is not None:  # 如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            auth.login(request, re)  # 登陆成功
            return redirect('/article', {'user': re})  # 跳转--redirect指从一个旧的url转到一个新的url
        else:  # 数据库里不存在与之对应的数据
            return render(request, 'login.html', {'login_error': '用户名或密码错误'})  # 注册失败
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def article(request):
    article_list = Article.objects.all()
    return render(request, 'article.html', {'article_list': article_list})


def detail(request, id):
    # print id
    try:
        article = Article.objects.get(id=id)
        # print type(article)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', locals())


def write(request):
    wr = novalForm(request.POST)  # 包含标题和内容
    if wr.is_valid():
        # 获取表单数据
        title = wr.cleaned_data['title']  # cleaned_data类型是字典，里面是提交成功后的信息
        content = wr.cleaned_data['content']

        User1 = User.objects.filter(username=request.user.username).first()

        if Article.objects.filter(title=title):
            return render(request, 'share2.html', {'title': title})
        else:
            # 添加到数据库
            Article.objects.create(title=title, content=content,user_id=User1)
            return redirect('/article/')  # 跳转--redirect指从一个旧的url转到一个新的url
    return render(request, 'write.html', {'wr': wr})


def update(request):

    article_update_list = Article.objects.filter(user_id=request.user.id).all()
    return render(request, 'article_update.html', {'article_update_list': article_update_list})

def update_detail(request, update):
    article = Article.objects.get(id=update)
    wr = novalForm(request.POST)  # 包含标题和内容
    if wr.is_valid():
        # 获取表单数据
        title = wr.cleaned_data['title']  # cleaned_data类型是字典，里面是提交成功后的信息
        content = wr.cleaned_data['content']

        Article.objects.filter(id=update).update(title=title, content=content)
        return redirect('/article/')  # 跳转--redirect指从一个旧的url转到一个新的url
    return render(request, 'update_detail.html', {'article':article})


def delete(request):

    article_delete_list = Article.objects.filter(user_id=request.user.id).all()
    return render(request, 'article_delete.html', {'article_delete_list': article_delete_list})


def delete_detail(request, delete):

    Article.objects.filter(id=delete).delete()
    return redirect('/article/')  # 跳转--redirect指从一个旧的url转到一个新的url


