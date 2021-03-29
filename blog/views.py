from django.shortcuts import render, get_object_or_404#import make notice
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')#this orders all the blogs in terms of latest updates ,[:5] is used to limit of viwerships like 5 blogs or so 
    #we can use Blog.objects.all() to get all
    return render(request, "blog/all_blogs.html", {"blogs": blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})