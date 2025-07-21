from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Product, CartItem

from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings


def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('store:home')
            else:
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
    return render(request, 'store/login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password != confirm:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            username = email.split('@')[0]
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('store:home')
    return render(request, 'store/signup.html')

def logout_view(request):
    logout(request)
    return redirect('store:login')

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('store:login')

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('store:cart')

@login_required
def cart_view(request):
    cart = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart)
    return render(request, 'store/cart.html', {'cart': cart, 'total_price': total_price})


def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/buy_now.html', {'product': product})

def chatbot_response(request):
    user_input = request.GET.get("q", "")

    try:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful e-commerce support assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content.strip()

    except Exception as e:
        print("OpenAI Error:", e)
        reply = "I'm having trouble connecting to support right now. Try again later."

    return JsonResponse({'response': reply})

