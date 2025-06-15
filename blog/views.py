from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def blogs(request):
    
    return render(request, "blogs.html")

def about(request):
    with open(r"static\python-depends.json",encoding='utf-16 le') as f:
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