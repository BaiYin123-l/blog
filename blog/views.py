from django.shortcuts import render
import json
from blog.update_github_repo import get_github_data
from blog.models import Blog

# Create your views here.
def index(request):
    # 获取 GitHub 数据
    github_data = get_github_data()
    return render(request, "index.html", {'github_data': github_data})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {'blogs':blogs})

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "blog.html", {'blog': blog})

def about(request):
    with open(r"static\python-depends.json",encoding='utf-8') as f:
        content = f.read()
        # 检查并移除 BOM
        if content.startswith('\ufeff'):
            content = content[1:]
        t1 = json.loads(content)
    with open(r"static\node-depends.json", encoding='utf-8') as f:
        content = f.read()
        # 检查并移除 BOM
        if content.startswith('\ufeff'):
            content = content[1:]
        t2 = json.loads(content)
    return render(request, "about.html", {'t1':t1, 't2':t2})