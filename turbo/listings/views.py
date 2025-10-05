from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Listing,ListingStatus
from .forms import ListingForm

# Create your views here.

def listings_list(request):
    qs=Listing.objects.filter(status=ListingStatus.APPROVED)

    q=request.GET.get('q') or ''
    city=request.GET.get('city') or ''
    brand=request.GET.get('brand') or ''
    minp=request.GET.get('min_price') or ''
    maxp=request.GET.get('max_price') or ''

    if q:
        qs=qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(model__icontains=q) | Q(brand__icontains=q))

    if city:
        qs=qs.filter(city__iexact=city)

    if brand:
        qs=qs.filter(brand__iexact=brand)

    if minp.isdigit():
        qs=qs.filter(price__gte=int(minp))

    if maxp.isdigit():
        qs=qs.filter(price__lte=int(maxp))

    context={
        'listings':qs.select_related('owner')[:100],
        'q':q,'city':city,'brand':brand,'minp':minp,'maxp':maxp
    }

    return render(request,'listings/listing_list.html',context)