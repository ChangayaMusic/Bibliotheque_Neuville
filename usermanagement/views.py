# views.py
from django.shortcuts import render, redirect
from usermanagement.forms import CustomUserCreationForm

def add_reader_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirection vers la page de succès
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_reader.html', {'form': form})
