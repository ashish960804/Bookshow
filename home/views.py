from django.shortcuts import render,HttpResponse
from movies.models import Movie

# Create your views here.

def show_index(request):
	movie_list = Movie.objects.all().order_by('popularity_index')
	top_movie = Movie.objects.all().order_by('popularity_index')[:3]

	return render(request, 'common/home.html', {'movie_list': movie_list, 
		'top_movie': top_movie})

def contact(request):
	return render(request, 'common/contact.html')

def about(request):
	return render(request, 'common/about.html')
