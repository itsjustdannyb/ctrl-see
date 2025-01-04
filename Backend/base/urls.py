from django.contrib import admin
from django.urls import path
from .views import TextDetailView, TextListView, TextCreateView, GetEditorView, textToSpeech, TextUpdateView


urlpatterns = [
    path('', TextListView.as_view(), name='text-list'),
    path('<int:pk>/', TextDetailView.as_view(), name='text-detail'),
    #path('getEditor/<int:pk>', GetEditorView.as_view(), name='get-editor'),
    path('editor/new/', TextCreateView.as_view(), name='text-create'),
    path('editor/<int:pk>/update/', TextUpdateView.as_view(), name='text-update'),
    path('textToSpeech/<int:pk>', textToSpeech, name='speech')
]