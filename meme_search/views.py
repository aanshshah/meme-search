from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from string import punctuation
# Create your views here.
def home(request):
    return render(request, 'index.html')

@csrf_exempt
def search(request):
    if request.method == 'POST':
        words = request.POST.get('keywords')
        words = strip_punctuation(words)
        words = words.split()
        context = {'results': words,
                   }
    return render_to_response('results.html', context)

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)