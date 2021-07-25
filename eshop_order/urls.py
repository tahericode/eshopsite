from eshop_order.views import add_user_order
from django.urls import path
from .views import add_user_order, user_open_order, remove_oreder_detail

urlpatterns = [
    path('add-user-order', add_user_order),
    path('open-order',user_open_order),
    path('remove-order-detail/<detail_id>',remove_oreder_detail),

]
