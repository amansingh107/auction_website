from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import AuctionItem
from .forms import AuctionItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import  Bid
from .forms import BidForm

@login_required
def main_page(request):
    # Any additional logic you might want to include
    return render(request, 'index.html')  # Renders the index.html template

@login_required
def list_item(request):
    if request.method == 'POST':
        form = AuctionItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('auctions:list_item')  # Redirect to user's dashboard
    else:
        form = AuctionItemForm()
    return render(request, 'list_item.html', {'form': form})

def browse_items(request):
    items = AuctionItem.objects.all()
    bid_form = BidForm()
    return render(request, 'browse_items.html', {'items': items, 'bid_form': bid_form})

@login_required
@login_required
def place_bid(request, item_id):
    item = get_object_or_404(AuctionItem, pk=item_id)
    current_highest_bid = item.highest_bid

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid_amount = form.cleaned_data['amount']
            if new_bid_amount > current_highest_bid:
                bid = form.save(commit=False)
                bid.item = item
                bid.bidder = request.user
                bid.save()
                item.highest_bid = new_bid_amount
                item.save()
                return redirect('auctions:browse_items')
    else:
        form = BidForm()

    return render(request, 'place_bid.html', {'item': item, 'form': form})


@login_required
def user_dashboard(request):
    user_items = AuctionItem.objects.filter(seller=request.user)
    return render(request, 'user_dashboard.html', {'user_items': user_items})


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(AuctionItem, pk=item_id, seller=request.user)
    if request.method == 'POST':
        form = AuctionItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('auctions:user_dashboard')
    else:
        form = AuctionItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

@login_required
def close_auction(request, item_id):
    item = get_object_or_404(AuctionItem, pk=item_id, seller=request.user)
    
    if request.method == 'POST':
        item.auction_status='closed'
        item.save()
        # Perform any other necessary actions here
        return redirect('auctions:user_dashboard')
    
    return render(request, 'list_item.html', {'item': item})
