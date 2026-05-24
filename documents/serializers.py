from rest_framework import serializers
from .models import QuestionHistory


class AskQuestionSerializer(serializers.Serializer):
    SEARCH_METHOD_CHOICES = [
        ("simple", "Simple Search"),
        ("bm25", "IR / BM25 Search"),
    ]

    question = serializers.CharField()

    search_method = serializers.ChoiceField(
        choices=SEARCH_METHOD_CHOICES,
        default="simple",
        required=False
    )


class QuestionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionHistory
        fields = [
            "id",
            "question",
            "answer",
            "retrieved_context",
            "created_at"
        ]