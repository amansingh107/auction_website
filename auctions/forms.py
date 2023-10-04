from django import forms
from .models import AuctionItem
from .models import Bid


class AuctionItemForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = ['title', 'description', 'starting_bid', 'image']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
