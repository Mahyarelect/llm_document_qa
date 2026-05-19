from rest_framework import serializers
from .models import QuestionHistory


class AskQuestionSerializer(serializers.Serializer):
    question = serializers.CharField()


class QuestionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionHistory
        fields = ['id', 'question', 'answer', 'retrieved_context', 'created_at']