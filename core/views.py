from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'core/home_modern.html')


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')
