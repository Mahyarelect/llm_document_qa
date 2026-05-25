from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from .models import QuestionHistory
from .serializers import AskQuestionSerializer, QuestionHistorySerializer
from .services import generate_answer

class AskQuestionAPIView(generics.GenericAPIView):
    serializer_class = AskQuestionSerializer
    renderer_classes = [
        JSONRenderer,
        BrowsableAPIRenderer
    ]
    parser_classes = [
        JSONParser,
        FormParser,
        MultiPartParser
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data["question"]
        search_method = serializer.validated_data.get("search_method", "simple")

        result = generate_answer(
            question=question,
            search_method=search_method
        )
        
        if not isinstance(result, dict):
            result = {
            "answer": "LLM service error: Invalid response from generate_answer().",
            "context": "",
            "search_method": search_method,
        }

        history = QuestionHistory.objects.create(
            question=question,
            answer=result["answer"],
            retrieved_context=result["context"]
        )

        return Response(
            {
                "question": question,
                "search_method": result["search_method"],
                "answer": result["answer"],
                "context": result["context"],
                "history_id": history.id,
            },
            status=status.HTTP_200_OK
        )


class QuestionHistoryListAPIView(generics.ListAPIView):
    queryset = QuestionHistory.objects.all().order_by(
        "-created_at"
    )

    serializer_class = QuestionHistorySerializer

    renderer_classes = [
        JSONRenderer,
        BrowsableAPIRenderer
    ]