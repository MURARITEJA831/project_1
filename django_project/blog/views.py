from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Murari',
        'title' :'Blog_post 1',
        'content': 'first post ',
        'date_posted':'jan 5 2021'
    },
    {
        'author':'teja',
        'title':'blog_post 2',
        'content':'2nd post',
        'date_posted':'jan 5 2021'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
