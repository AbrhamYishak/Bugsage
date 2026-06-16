from django.urls import path
from .views import ErrorTypeView, ErrorCaseView, upvote, downvote
urlpatterns = [
    path('errortype',ErrorTypeView.as_view()),
    path('errorcase', ErrorCaseView.as_view()),
    path('upvote/<int:pk>', upvote),
    path('downvote/<int:pk>',downvote)
]
