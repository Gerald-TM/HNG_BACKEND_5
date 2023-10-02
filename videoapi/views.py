from django.http import JsonResponse
from .models import Video
from rest_framework import generics
from .serializers import VideoSerializer

def upload_video_chunk(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        title = request.POST.get('title')
        chunk_number = request.POST.get('chunk_number')
        data = request.FILES['video_chunk'].read()

        video_chunk = Video(session_id=session_id,title=title, chunk_number=chunk_number, data=data)
        video_chunk.save()

        return JsonResponse({'message': 'Video chunk uploaded successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer