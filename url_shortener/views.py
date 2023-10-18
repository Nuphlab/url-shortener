from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import ShortenedURL
from rest_framework import viewsets
from .serializers import ShortenedURLSerializer
import validators, hashlib

class ShortenedURLViewSet(viewsets.ModelViewSet):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # Validate our URL
        if not validators.url(url):
            return JsonResponse({'error': 'Invalid URL'}, status=400)
        short_url = make_short_url(url)
        ShortenedURL.objects.create(original_url=url, short_url=short_url)
        return JsonResponse({'shortUrl': short_url})
    return render(request, 'index.html')

def make_short_url(url):
    hash_object = hashlib.md5(url.encode())
    hex_dig = hash_object.hexdigest()
    short_url = hex_dig[:8]  # set length of short url
    return short_url # host will be added automatically

def get_original_url(request, short_url):
    print(request)
    shortened_url = get_object_or_404(ShortenedURL, short_url=short_url)
    return HttpResponseRedirect(shortened_url.original_url)

def error_status_404(request, exception):
    return JsonResponse({'error': 'Short URL was not found.'}, status=404)