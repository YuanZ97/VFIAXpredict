from django.shortcuts import render

def first_temp(request):
    #values = Price.objects.all()
    return render(request, 'frontend.html', {'test'})
