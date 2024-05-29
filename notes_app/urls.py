from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_all_notes, name="view_all_notes"),
    path("add/", views.create_note, name="create_note"),
    path("note/<int:note_id>/", views.view_note, name="view_note"),
    path("edit/<int:note_id>/", views.edit_note, name="edit_note"),
    path("note/delete/<int:note_id>/", views.delete_note, name="delete_note"),
]
