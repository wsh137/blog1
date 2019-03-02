from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()#위에서 각 객체에 저장받은 데이터를 저장하라는 메소드
    return redirect('/blog/'+str(blog.id))
    #db에 저장되고 저 url로 이동된다. redirect는 안에 url을 치면 거기로 간다
