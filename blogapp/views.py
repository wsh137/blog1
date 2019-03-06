from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost
def home(request):
    blogs = Blog.objects #쿼리셋
    #블로그 모든 글(객체)들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 4)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})


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

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 --> POST 방식
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #저장하지 않고 모델 객체를 가지고 온다, post는 블로그형 객체
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 --> GET 방식
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})