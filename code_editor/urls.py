from django.urls import path
from code_editor.views import  *

urlpatterns = [
    path('', CodeEditor.as_view()),
    path('code_output', CodeOutput.as_view())
]