from django.shortcuts import render, redirect, HttpResponse
from cartt.models import ContactUs, CartItem
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm


# Create your views here.


def login(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def checkout_success(request):
    return render(request, 'checkout_success.html')


@login_required(login_url='/login/')
def cart(request):
    return render(request, 'cart.html')


@login_required(login_url='/login/')
def orders(request):
    return render(request, 'orders.html')

@login_required(login_url='/login/')
def wishlist(request):
    return render(request, 'wishlist.html')


@login_required(login_url='/login/')
def blog(request):
    return render(request, 'blog.html')


@login_required(login_url='/login/')
def base(request):
    return render(request, 'base.html')


@login_required(login_url='/login/')
def mail(request):
    return render(request, 'mail.php')


@login_required(login_url='/login/')
def shop_now(request):
    return render(request, 'shop_now.html')
    

@login_required(login_url='/login/')
def checkout(request):
     if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        postal_code = request.POST.get('postal_code')
        total_price = request.POST.get('total_price')

        total_price_str = request.POST.get('total_price', '0.00')
        try:
            total_price = Decimal(total_price_str.replace('$', '').replace(',', ''))
        except InvalidOperation:
            # Handle invalid decimal conversion
            total_price = Decimal('0.00')



        # Retrieve or create a customer
        customer, created = Customer.objects.get_or_create(user=request.user)


        # Create the Order instance
        order = Order(
            customer=customer,
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            country=country,
            add1=add1,
            add2=add2,
            postal_code=postal_code,
            total_price=total_price, 
        )
        order.save()


 # Retrieve cart items and create OrderItem instances
        cart_items = CartItem.objects.filter()
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            # Optionally, remove the cart item after order creation
            item.delete()

         

        return redirect('checkout_success')  

        cart_items = []  # Replace with actual cart items retrieval logic
        total = Decimal('0.00')  # Replace with actual total calculation logic

        return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})


@login_required(login_url='/login/')
def contact(request):
    if request.method == 'POST':
        contact = ContactUs(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message  = request.POST.get('message'),
        )
        contact.save()
    return render(request, 'contact.html')
    


@login_required(login_url='/login/')
def customer_profile(request):
    customer, created = Customer.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customer_profile.html', {'form': form})

@login_required(login_url='/login/')
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('customer_profile')
    else:
        form = CustomerForm()
    
    return render(request, 'customer_create.html', {'form': form})

@login_required(login_url='/login/')
def customer_update(request):
    customer = Customer.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customer_update.html', {'form': form})