from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    notes = Note.objects.all().order_by('-id')
    return render(request, 'notes.html', {'notes': notes})


def note_detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'note_detail.html', {'note': note})


def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    notes = Note.objects.all().order_by('-id')
    render(request, 'notes.html', {'notes': notes})
    return redirect('/')

