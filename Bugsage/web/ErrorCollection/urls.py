from django.urls import path
from .views import ErrorTypeView, ErrorCaseView
urlpatterns = [
    path('errortype',ErrorTypeView.as_view()),
    path('errorcase', ErrorCaseView.as_view())
]
