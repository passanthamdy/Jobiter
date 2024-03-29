from django.urls import path
from .views import create_review,get_list_of_reviews,review_details
app_name='reviews'


urlpatterns = [
    path('<int:id>/create-review/',create_review,name="create_review"),
    path('<int:id>/get-all-reviews/',get_list_of_reviews,name="get_all_reviews"),
    path('get-review-details/<int:review_id>/',review_details,name="get_review_details"),
    # path('edit-review/<int:review_id>/',edit_review,name="edit_review"),
    # path('delete-review/<int:review_id>/',delete_review,name="delete_review"),
]