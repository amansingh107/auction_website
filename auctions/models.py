from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model


class AuctionItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='item_images/' ,default="598846.jpg")  # Add the image field
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    auction_status = models.CharField(max_length=10, default='open')

    def __str__(self):
        return self.title
    
User = get_user_model()

class Bid(models.Model):
    item = models.ForeignKey('AuctionItem', on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bid on {self.item} by {self.bidder} for ${self.amount}'


