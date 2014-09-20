# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the forensic index.")

def detail(request, user_id):
    return HttpResponse("You're looking at the %s." % user_id)
def results(request, user_id):
    return HttpResponse("You're looking at the results of user %s." % user_id)
def play(request, user_id):
    return HttpResponse("You're playing as user %s." % user_id)



