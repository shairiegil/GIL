from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json

    news_api_request= requests.get(
        "http://newsapi.org/v2/everything?q=tesla&from=2021-01-15&sortBy=publishedAt&apiKey=48b194b6843042eabc1dcf304f3a8cc6"
    )
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api':api})