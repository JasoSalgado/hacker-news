"""apps/story/views.py"""

# Django modules
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# my modules
from .forms import StoryForm, CommentForm
from .models import Story, Vote, Comment
from .my_captcha import FormWithCaptcha

def captcha(request):
    context = {
        'captcha': FormWithCaptcha,
    }
    return render(request, 'story/frontpage.html', context)

def frontpage(request):
    # It shows the best posts
    date_form = datetime.datetime.now() - datetime.timedelta(days=1)

    stories = Story.objects.filter(created_at__gte=date_form).order_by('-number_of_votes')
    return render(request, 'story/frontpage.html', {'stories': stories})


def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        stories = Story.objects.filter(title__icontains=query)
    else:
        stories = []
    
    return render(request, 'story/search.html', {'stories': stories, 'query': query})


def story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()

            return redirect('story', story_id=story_id)
    else:
        form = CommentForm()

    return render(request, 'story/detail.html', {'story': story,'form': form})


def newest(request):
    stories = Story.objects.all()[0:200]

    return render(request, 'story/newest.html', {'stories': stories})


@login_required
def vote(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    next_page = request.GET.get('next_page', '')

    if story.created_by != request.user and not Vote.objects.filter(created_by=request.user, story=story):
        vote = Vote.objects.create(story=story, created_by=request.user)
    
    if next_page == 'story':
        return redirect('story', story_id=story_id)
    else:
        return redirect('frontpage')

    return redirect('frontpage')


@login_required
def submit(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()

            return redirect('frontpage')

    else:
        form = StoryForm()

    return render(request, 'story/submit.html', {'form': form})