from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import lotto
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# import json

# Create your views here.

def index_page(request):
    return render(request, "lotto/index.html")