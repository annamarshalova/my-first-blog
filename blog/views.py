from django.shortcuts import render, get_object_or_404, redirect
import random
from .models import Post, Video
from django.utils import timezone
from .forms import PostForm, VideoForm
import re
arr=[]
planets = [{"name": "Меркурий", "description": "", "points": 0}, {"name": "Венера", "description": "", "points": 0},
               {"name": "Земля", "description": "", "points": 0}, {"name": "Марс", "description": "", "points": 0},
               {"name": "Юпитер", "description": "", "points": 0}, {"name": "Сатурн", "description": "", "points": 0},
               {"name": "Уран", "description": "", "points": 0}, {"name": "Нептун", "description": "", "points": 0}]
def main(request):
    return render(request, 'blog/main.html', {})
def mercury(request):
    return render(request, 'blog/1.html', {})
def venus(request):
    return render(request, 'blog/2.html', {})
def earth(request):
    return render(request, 'blog/3.html', {})
def mars(request):
    return render(request, 'blog/4.html', {})
def jupiter(request):
    return render(request, 'blog/5.html', {})
def saturn(request):
    return render(request, 'blog/6.html', {})
def uranus(request):
    return render(request, 'blog/7.html', {})
def neptune(request):
    return render(request, 'blog/8.html', {})
def other(request):
    return render(request, 'blog/other.html', {})
def videos(request):
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/videos.html', {'videos':videos})
def test(request):
    return render(request, 'blog/test.html', {})

def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts,'total_posts': len(posts)})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            words = post.text.split(' ')[:50]
            post.shorttext = ' '.join(words)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            words=post.text.split(' ')[:50]
            post.shorttext = ' '.join(words)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts')

def video_new(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            #video.link=re.sub(r'watch?v=',r'embed/', video.link)
            #video.author = request.user
            video.published_date = timezone.now()
            video.save()
            return redirect('videos')
    else:
        form = VideoForm()
    return render(request, 'blog/video_edit.html', {'form': form})
#from .forms import UserForm

from django.shortcuts import HttpResponse

def search (request):
    search_results = []
    posts_number=-1
    try:
        search=request.GET["search"]
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        for post in posts:
            if search.lower() in post.text.lower().split(" "):
                    search_results.append(post)
        posts_number=len(search_results)
        #return HttpResponse(search_results)
    finally:
        return render(request, 'blog/search.html', {'search_results':search_results,'posts_number':posts_number})

def test_1(request):
    for pl in planets:
        pl["points"]=0
    return render(request, 'blog/test_1.html', {})
#with open('/static/planets.json') as js:
    #planets=json.load(js)
def test_2(request):
    try:
        val=request.GET["color"]
    except:
        val = random.randint(0, 7)
    planets[int(val)]["points"]+=1
    return render(request, 'blog/test_2.html', {})

def test_3(request):
    try:
        val=request.GET["friends"]
    except:
        val = random.randint(0, 6)
    planets[int(val)]["points"]+=1
    planets[int(val)+1]["points"] += 1
    return render(request, 'blog/test_3.html', {})

def test_4(request):
    try:
        val=request.GET["season"]
    except:
        val = random.randint(0, 6)
    planets[int(val)]["points"]+=1
    planets[int(val)+1]["points"] += 1
    return render(request, 'blog/test_4.html', {})
def test_5(request):
    try:
        val=request.GET["quality"]
    except:
        val = random.randint(0, 7)
    planets[int(val)]["points"]+=1
    return render(request, 'blog/test_5.html', {})
def test_6(request):
    try:
        val=request.GET["day"]
    except:
        val = random.randint(0, 7)
    planets[int(val)]["points"]+=1
    return render(request, 'blog/test_6.html', {})
def test_7(request):
    try:
        val=request.GET["subject"]
    except:
        val = random.randint(0, 7)
    planets[int(val)]["points"]+=1
    return render(request, 'blog/test_7.html', {})
def test_8(request):
    try:
        val=request.GET["country"]
    except:
        val = random.randint(0, 7)
    planets[int(val)]["points"]+=1
    return render(request, 'blog/test_8.html', {})

def counting(request):
    try:
        val=request.GET["pet"]
    except:
        val = random.randint(0, 7)
    planets[int(val)]["points"]+=1
    allpoints=[planets[i]["points"] for i in range(0,8)]
    maxpoint=max(allpoints)
    if allpoints.count(maxpoint)==1:
        yourplanet=allpoints.index(maxpoint)
    else:
        maxpoints=[]
        for i in allpoints:
            if i==maxpoint:
                maxpoints.append(allpoints.index(i))
        yourplanet = random.choice(maxpoints)
    #return HttpResponse(planets)
    return render(request, 'blog/counting.html',{'yourplanet': yourplanet})
def result(request):
    yourplanet=request.GET["yourplanet"]
    return render(request, 'blog/result.html', {'yourplanet': yourplanet})



def handler404(request,exception):
    return render(request, '404.html',status=404)


