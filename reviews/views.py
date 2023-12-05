from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self,request):
        reviews = []
        for review in Review.objects.filter():
            reviews.append(review.review_text)
        return Response({'reviews': reviews})
    
class CreateAppDevClubReview(APIView):
    def post(self, request):
        review = request.data.get('review')

        if review == '':
            return Response({'message:' 'Failure'})
        else:
            new_database_entry = Review(review_text=review)
            new_database_entry.save()
            return Response({'message': 'Review added'})
    
    