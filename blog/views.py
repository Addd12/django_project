from django.db import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # sorts in descending order, meaning from the latest post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #login is required before creating a post so we use LoginRequiredMixin, we cannot use decorators bcs it's a class, not a function
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): # this method is used to connect the new post with the author that is creating it (the logged in user)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # UserPassesTestMixin is used to check if the updater is the actual author IMPORTANT! otherwise other users can update you post 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # check if the logged in user is the author
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # LoginRequiredMixin, UserPassesTestMixin have to be on the left (before) DeleteView otherwise other users can access the posts without passing the test and login
    model = Post
    success_url = '/' # when this line is missing, after the post deletion there's an error bcs it doesn't know where to redirect

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
