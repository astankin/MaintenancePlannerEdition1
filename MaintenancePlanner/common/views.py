from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'common/home-page.html')
    return render(request, 'common/index.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)
