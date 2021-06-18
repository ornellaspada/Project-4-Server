from django.db.models.fields import BooleanField
from django.http.response import JsonResponse
from rest_framework.fields import NullBooleanField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Runaway, Comment, Rental
from .serializers import (
  RunawaySerializer, 
  PopulatedRunawaySerializer, 
  CommentSerializer, 
  RentSerializer, 
  PopulatedRentalSerializer,
  PurchaseSerializer,
)

from datetime import date
# Create your views here.
class RunawayListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        runaways = Runaway.objects.all()
        serialized_runaways = PopulatedRunawaySerializer(runaways, many=True)
        return Response(serialized_runaways.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request.data['owner'] = request.user.id
        new_runaway = RunawaySerializer(data=request.data)
        if new_runaway.is_valid():
            new_runaway.save()
            return Response(new_runaway.data, status=status.HTTP_201_CREATED)
        return Response(new_runaway.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class RunawayDetailView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_runaway(self, pk):
        try:
            return Runaway.objects.get(pk=pk)
        except Runaway.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        runaway = self.get_runaway(pk=pk)
        serialized_runaway = PopulatedRunawaySerializer(runaway)
        return Response(serialized_runaway.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        runaway_to_update = self.get_runaway(pk=pk)
        # if runaway_to_update.owner != request.user:
        #   raise PermissionDenied()
        # request.data['owner'] = request.user.id
        updated_runaway = RunawaySerializer(runaway_to_update, data=request.data)
        if updated_runaway.is_valid():
            updated_runaway.save()
            return Response(updated_runaway.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_runaway.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)    
    
    def delete(self, _request, pk):
        runaway_to_delete = self.get_runaway(pk=pk)
        # if runaway_to_delete.owner != request.user:
        #     raise PermissionDenied()
        runaway_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RunawayFavoriteView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        try:
            runaway_to_favorite = Runaway.objects.get(pk=pk)
            if request.user in runaway_to_favorite.favorited_by.all():
                runaway_to_favorite.favorited_by.remove(request.user.id)
            else:
                runaway_to_favorite.favorited_by.add(request.user.id)
            runaway_to_favorite.save()
            serialized_runaway = PopulatedRunawaySerializer(runaway_to_favorite)
            return Response(serialized_runaway.data, status=status.HTTP_202_ACCEPTED)
        except Runaway.DoesNotExist:
            raise NotFound()

class CommentListView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, run_pk):
        request.data['runaway'] = run_pk
        request.data['owner'] = request.user.id
        serialized_comment = CommentSerializer(data=request.data)
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_201_CREATED)
        return Response(serialized_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CommentDetailView(APIView):

    def delete(self, request, _run_pk, comment_pk):
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            if comment_to_delete.owner != request.user:
                raise PermissionDenied()
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound() 

class RunawayRentalView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, run_pk):
        data = {
          "date_rented": date.today(),
          "rented": True,
          "date_returned": request.data['date_returned']
        }
        data['runaway'] = run_pk
        data['owner'] = request.user.id
        serialized_rental = RentSerializer(data=data)
        if serialized_rental.is_valid():
            serialized_rental.save()
            return Response(serialized_rental.data, status=status.HTTP_201_CREATED)
        return Response(serialized_rental.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def put(self, request, rental_pk):
        try:
            return_to_update = Rental.objects.get(pk=rental_pk)
            if return_to_update.owner != request.user:
                raise PermissionDenied()
            rental = RentSerializer(return_to_update, data=request.data)
            if rental.is_valid():
              rental.save()
              return Response(rental.data, status=status.HTTP_202_ACCEPTED)
            return Response(rental.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Comment.DoesNotExist:
            raise NotFound() 

class RunawayPurchaseView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, run_pk):
        data = {
          "date_purchased": date.today(),
        }
        data['runaway'] = run_pk
        data['owner'] = request.user.id
        serialized_purchase = PurchaseSerializer(data=data)
        if serialized_purchase.is_valid():
            serialized_purchase.save()
            return Response(serialized_purchase.data, status=status.HTTP_201_CREATED)
        return Response(serialized_purchase.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)



