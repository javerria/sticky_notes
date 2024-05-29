from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import StickyNote
import random


# View to list all sticky notes
def view_all_notes(request):
    notes = StickyNote.objects.all()
    rotation_classes = ["rotate-1", "rotate-2"]
    for note in notes:
        note.rotation_class = random.choice(rotation_classes)
    return render(request, "index.html", {"notes": notes})


# View to display a single sticky note
def view_note(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    return render(request, "view_note.html", {"note": note})


# View to create a new sticky note
def create_note(request):
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        StickyNote.objects.create(author=author, title=title, content=content)
        return redirect("view_all_notes")
    return render(request, "add_note.html")


# View to edit an existing sticky note
def edit_note(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        note.author = author
        note.title = title
        note.content = content
        note.save()
        return redirect("view_note", note_id=note.id)
    return render(request, "edit_note.html", {"note": note})


# View to delete an existing sticky note
def delete_note(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    note.delete()
    return redirect("view_all_notes")
