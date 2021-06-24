from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, UserList, UserDetail

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
    Including format_suffix_patterns is an optional choice that provides a simple, 
    DRY way to refer to a specific file format for a URL endpoint. 
    It means our API will be able to handle URls such as http://example.com/api/items/4.json 
    rather than just http://example.com/api/items/4.
"""