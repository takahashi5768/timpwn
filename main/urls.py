from django.urls import path
from . import views

"""
Note:
    One the day of the event comment or get rid of the line marked with the comment
to prevent people from adding data into the server
"""

urlpatterns = [
    path('get/', views.get_, name="get_data"),
]
