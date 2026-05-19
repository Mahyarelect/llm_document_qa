from django.urls import path
from .views import AskQuestionAPIView, QuestionHistoryListAPIView


urlpatterns = [
    path('ask/', AskQuestionAPIView.as_view(), name='ask-question'),
    path('history/', QuestionHistoryListAPIView.as_view(), name='question-history'),
]