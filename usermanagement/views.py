# views.py

from django.shortcuts import render, redirect
from usermanagement.forms import CustomUserCreationForm

def add_reader_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the home page
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_reader.html', {'form': form})
