from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def available_movies(request):


    data = {'movies':['Little Hearts','OG','Demon Slayer', 'Mirai', 'KGF2'],
            'upcoming':'Rajsaab',
            'movies_with_issues':['OG','Demon Slayer', 'Mirai']
            
            
            }

    return render(request, 'movies.html', context = data)





def add(request, a, b):
        # print(id+id2)
        data = {'sum': a+b}
        return render(request, 'sum.html', context = data)