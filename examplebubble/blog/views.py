from django.shortcuts import render
from django.http import HttpResponse

#dummy data
dums = [{'name': 'val1',
	 'born': 'August 28, 2018',
	 'status': 'Single'},
	{'name': 'val2',
	 'born': 'December 28, 2000',
	 'status': 'Married'}
]


# Create your views here.

def home(request):
	context = {
	  'people': dums
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')
