from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406428876',
        'name': 'Khayra Tazkiya',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)