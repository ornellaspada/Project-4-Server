from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Purchase, Rental, Runaway, Comment
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image' )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class RunawaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Runaway
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    owner = UserSerializer()

class PopulatedPurchaseSerializer(PurchaseSerializer):
    runaway = RunawaySerializer()

class PopulatedRentalSerializer(RentSerializer):
    runaway = RunawaySerializer()
  
class PopulatedRunawaySerializer(RunawaySerializer):
    comments = PopulatedCommentSerializer(many=True)
    rentals = PopulatedRentalSerializer(many=True)
    favorited_by = UserSerializer(many=True)



    # owner = UserSerializer()










