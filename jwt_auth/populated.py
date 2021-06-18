from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from runaways.serializers import PurchaseSerializer, RunawaySerializer, RentSerializer, PopulatedRentalSerializer, PopulatedPurchaseSerializer
from runaways.serializers import CommentSerializer

User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    favorites = RunawaySerializer(many=True)
    comments = CommentSerializer(many=True)
    rentals= PopulatedRentalSerializer(many=True)
    purchases= PopulatedPurchaseSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'profile_image',
            'email',
            'favorites',
            'comments', 
            'rentals',
            'purchases',
        )
