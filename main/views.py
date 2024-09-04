from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165502',
        'name': 'Rama Aditya Rifki Harmono',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
