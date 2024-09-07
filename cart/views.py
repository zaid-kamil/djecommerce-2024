from django.shortcuts import render, redirect

def show_cart(request):
    return render(request, 'cart/show.html')

def success(request):
    return render(request, 'cart/success.html')

def failure(request):
    return render(request, 'cart/failure.html')

def orders(request):
    return render(request, 'cart/orders.html')

def add_product(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def remove_product(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def increase_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def decrease_qty(request, product):
    referrer = request.META.get('HTTP_REFERER')
    return redirect(referrer)

def checkout(request):
    pass