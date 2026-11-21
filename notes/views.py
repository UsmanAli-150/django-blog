from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
# Create your views here.

def note_list(request):
    notes = Note.objects.all().order_by("-created")
    return render(request,"notes/note_list.html",{"notes":notes})

def note_detail(request,pk):
    note = get_object_or_404(Note,pk=pk)
    return render(request,"notes/note_detail.html",{"note":note})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request,"notes/note_form.html",{"form":form})

def edit_note(request,pk):
    note = get_object_or_404(Note, pk = pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request,"notes/note_form.html",{"form":form})

def delete_note(request,pk):
    note = get_object_or_404(Note,pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request,"notes/note_confirm_delete.html",{"note":note})

def important_notes(request):
    notes = Note.objects.filter(is_important=True).order_by("-created")
    return render(request,"notes/note_list.html",{"notes":notes})