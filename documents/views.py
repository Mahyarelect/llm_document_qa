from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuestionHistory
from .serializers import (
    AskQuestionSerializer,
    QuestionHistorySerializer
)
from .services import generate_answer


class AskQuestionAPIView(APIView):

    def post(self, request):
        serializer = AskQuestionSerializer(data=request.data)

        if serializer.is_valid():
            question = serializer.validated_data['question']

            result = generate_answer(question)

            history = QuestionHistory.objects.create(
                question=question,
                answer=result['answer'],
                retrieved_context=result['context']
            )

            return Response({
                "question": question,
                "answer": result['answer'],
                "context": result['context'],
                "history_id": history.id
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class QuestionHistoryListAPIView(APIView):

    def get(self, request):
        history = QuestionHistory.objects.all().order_by('-created_at')

        serializer = QuestionHistorySerializer(
            history,
            many=True
        )

        return Response(serializer.data)
