from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("이제 일을 시작해볼까\n깃 다루는 것도 이해해야 되네")

