from django.shortcuts import render
from .forms import BookingForm

def form_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})
