from django.shortcuts import render

def home(request):
    news = Product.objects.all()
    return render(request, 'home.html', context={'news_list': news})