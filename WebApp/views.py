from django.http import HttpResponse
from django.shortcuts import render


def contact(request):
    return render(request,'contact.html')

# def about(request):
#     data={
#         'title':'about-us',
#         'data':'this is an data',
#         'clist':['PHP','Java','Django'],
#         'details':[
#             {'name':'abhi','phone':'3809724402'},
#             {'name':'raf','phone':'3809322302'}
#         ]
#     }
#     return render(request,'about.html',data)
def about(request):
    return render(request,'about.html')


def homepage(request):
    return render(request,'homepage.html')

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def index_page(request): 
    return render(request,'index.html')