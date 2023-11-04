from django.shortcuts import render, redirect, get_object_or_404
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
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            note.title = title
            note.content = content
            note.save()
            return redirect('/')

    return render(request, 'note_detail.html', {'note': note})


def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    notes = Note.objects.all().order_by('-id')
    render(request, 'notes.html', {'notes': notes})
    return redirect('/')

