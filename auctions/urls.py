from django.urls import path
from .views import close_auction, edit_item, list_item, browse_items, main_page, place_bid,user_dashboard



app_name = 'auctions'

urlpatterns = [
    # Other URL patterns...
    path('main_page/', main_page, name='main_page'),
    path('list_item/', list_item, name='list_item'),
    path('browse_items/', browse_items, name='browse_items'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('place_bid/<int:item_id>/', place_bid, name='place_bid'),
    path('edit_item/<int:item_id>/', edit_item, name='edit_item'),
    path('close_auction/<int:item_id>/', close_auction, name='close_auction'),
]



