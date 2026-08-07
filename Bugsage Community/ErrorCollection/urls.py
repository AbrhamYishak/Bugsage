from django.urls import path
from .views import ErrorTypeView, ErrorCaseView, upvote, downvote,ErrorCaseExists,ErrorTypeExists
urlpatterns = [
    path('errortype',ErrorTypeView.as_view()),
    path('errorcase', ErrorCaseView.as_view()),
    path('errortypeexists', ErrorTypeExists),
    path('errorcaseexists', ErrorCaseExists),
    path('upvote/<int:pk>', upvote),
    path('downvote/<int:pk>',downvote)
]
