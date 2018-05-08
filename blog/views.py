from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
       #name = 'Djangp'
       # return HttpResponse('''<h1>Hello {myname}</h1>'''.format(myname=name))
       #return render(request, 'blog/post_list.html')
       posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
       return render(request, 'blog/post_list.html',{'posts':posts })