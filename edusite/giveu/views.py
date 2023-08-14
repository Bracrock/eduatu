from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("이제 일을 시작해볼까")

