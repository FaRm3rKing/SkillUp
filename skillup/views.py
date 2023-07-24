from django.shortcuts import render


def temp_home(request):
    return render(request, 'test.html')
