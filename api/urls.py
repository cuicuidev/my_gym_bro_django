from django.urls import path
from . import views

urlpatterns = [
    path('get_entries/', views.GetEntries.as_view()),
    path('get_entry/', views.GetEntry.as_view()),
    path('post_entry/', views.PostEntry.as_view()),
    path('put_entry/', views.PutEntry.as_view()),
    path('delete_entry/', views.DeleteEntry.as_view()),
]