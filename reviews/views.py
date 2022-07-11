from django.shortcuts import render
from rest_framework import status
from reviews.serializers import ReviewSerializer,UpdateReviewSerializer
from reviews.models import Review
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from reviews.permissions import MyPermission

# Create your views here.


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated ])
def get_list_of_reviews(request):
        reviewsList=Review.objects.all()
        reviewsSerializer=ReviewSerializer(reviewsList,many=True)
        return Response(reviewsSerializer.data)
    
@api_view(["POST"])  
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,MyPermission ])  
def create_review(request):
        reviewSerializer=ReviewSerializer(data=request.data)
        if reviewSerializer.is_valid():
            reviewSerializer.save()
            return Response(reviewSerializer.data,status=status.HTTP_201_CREATED)
        return Response(reviewSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,MyPermission ])
def review_details(request, review_id):
    reviewDetails = Review.objects.get(pk=review_id)
    reviewSerializer = ReviewSerializer(reviewDetails)
    return Response(data=reviewSerializer.data, status=status.HTTP_200_OK)

@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,MyPermission ])
def delete_review(request,review_id):
            reviewDetails = Review.objects.get(pk=review_id)
            reviewDetails.delete()
            return Response({"Message": "Review Is Deleted Successfully"}, status=status.HTTP_200_OK)


@api_view(["PUT","PATCH"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,MyPermission ])
def edit_review(request,review_id):
        reviewDetails = Review.objects.get(pk=review_id)
        reviewSerializer=UpdateReviewSerializer(reviewDetails,data=request.data,partial=True)
        if reviewSerializer.is_valid():
                reviewSerializer.save()
                return Response(reviewSerializer.data, status=status.HTTP_200_OK)
        return Response(reviewSerializer.errors, status=status.HTTP_400_BAD_REQUEST)





