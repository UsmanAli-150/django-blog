from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.note_list,name="note_list"),
    path('notes/<int:pk>/',views.note_detail,name="note_detail"),
    path('notes/new/',views.create_note,name="note_create"),
    path('notes/<int:pk>/edit/',views.edit_note,name="note_edit"),
    path('notes/<int:pk>/delete/',views.delete_note,name="note_delete"),
    path('notes/important/',views.important_notes,name="important_notes")
]
