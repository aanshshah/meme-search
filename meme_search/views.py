from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def search(request):
    #get search term
    #parse through search terms
    #create a score based system to return the search results
    #return a queried list of search images from database
    return render(search, 'results.html')