from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import Tweet

def tweet_list_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tweet_list_create')  # Redirect to avoid resubmission
    else:
        form = TweetForm()  # for GET request

    tweets = Tweet.objects.all().order_by('-created_at')  # Get all tweets

    # This will render your home.html template with form and tweets
    return render(request, 'home.html', {
        'form': form,
        'tweets': tweets
    })
