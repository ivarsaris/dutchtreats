from django.shortcuts import render

# Create your views here.
def about(request):
    """display about page"""

    return render(request, 'about.html')

def contact(request):
    """display contact page"""

    return render(request, 'contact.html')