from django.shortcuts import redirect
from django.urls import reverse

def redirect_view(a):
    return redirect(reverse('funds:report'))
