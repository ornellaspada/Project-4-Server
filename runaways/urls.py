from django.urls import path
from .views import (
  RunawayListView, 
  RunawayDetailView, 
  CommentListView, 
  CommentDetailView, 
  RunawayFavoriteView, 
  RunawayRentalView,
  RunawayPurchaseView,
)


urlpatterns = [
    path('', RunawayListView.as_view()),
    path('<int:pk>/', RunawayDetailView.as_view()),
    path('<int:pk>/favorite/', RunawayFavoriteView.as_view()),
    path('<int:run_pk>/rent/', RunawayRentalView.as_view()),
    path('<int:rental_pk>/return/', RunawayRentalView.as_view()),
    path('<int:run_pk>/purchase/', RunawayPurchaseView.as_view()),
    path('<int:run_pk>/comments/', CommentListView.as_view()),
    path('<int:_run_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
]
