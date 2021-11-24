from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'Ada',
#         'title': 'First title', 
#         'content': 'First post content', 
#         'date_posted': 'November 22, 2021'
#     },
#     {
#         'author': 'Nadi',
#         'title': 'Second title', 
#         'content': 'Second post content', 
#         'date_posted': 'November 23, 2021'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all() # posts list (above) was here before cresting the db, now we get the data from the db 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
