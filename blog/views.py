from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from .models import Post

# Create your views here.
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'published']


    def new_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.slug = slugify(new_post.title)
                new_post.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            form = PostForm()
        return render(request, "new_post.html", {'form': form})