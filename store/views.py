
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse


def home(request):
    products = Product.objects.all()
    cart = request.session.get("cart", {})

    return render(request, "store/home.html", {
    "products": products,
    "cart": cart
})


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    cart[product_id] = cart.get(product_id, 0) + 1

    request.session["cart"] = cart

    return redirect("home")

def cart_view(request):
    cart = request.session.get("cart", {})

    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        quantity = cart.get(str(product.id), 0)
        subtotal = product.price * quantity

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })

        total += subtotal

    return render(request, "store/cart.html", {
        "cart_items": cart_items,
        "total": total
    })


def rabin(request,roll_no):
    return HttpResponse(f"<h1> you roll no is :{roll_no}    </h1>")
