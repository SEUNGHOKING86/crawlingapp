from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import lotto
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# import json
# Create your views here.
import requests
from bs4 import BeautifulSoup



def index_page(request):
    return render(request, "lotto/index.html")


def lotto(request):
    if request.method == 'POST':
        html = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=900')
        soup = BeautifulSoup(html.text, 'html.parser')

        data1 = soup.find('div', {'class': 'win_result'})
        data1

        i = 0
        for i in range(0,7) :
            data2 = data1.findAll('span')[i].text
            lotto = open("로또 번호.txt", "a")
            lotto.write(data2 + ",")
            lotto.close()

            i = i + 1

        return render(request, "lotto/index.html", context={'data' : data2})


def weather(request):
    if request.method == 'POST':
        url = 'https://weather.naver.com/today/02150101'
        response = requests.get(url)
        text = response.text
        soup = BeautifulSoup(text)

        for i in soup.select_one('div.weather_area'):
            blind = soup.select_one('div.weather_area')
            data = blind.text.replace('\n', '')
        print(data)
        return render(request, 'lotto/index.html', context={'data': data})








    # if request.method == 'GET':





    # from bs4 import BeautifulSoup
    # import requests

    # html = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=900')
    # pprint(html.text)

    # soup = BeautifulSoup(html.text, 'html.parser')
    #
    # data1 = soup.find('div', {'class': 'win_result'})
    #
    # i = 0
    # for i in range(0, 7):
    #     data2 = data1.findAll('span')[i].text
    #     lotto = open("로또 번호.txt", "a")
    #     lotto.write(data2 + ",")
    #     lotto.close()
    #
    #     i = i + 1
    #     print(i)