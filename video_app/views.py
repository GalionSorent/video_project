from django.shortcuts import render
from .models import Video, Comment

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_app/video_list.html', {'videos': videos})

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    comments = Comment.objects.filter(video=video)
    return render(request, 'video_app/video_detail.html', {'video': video, 'comments': comments})