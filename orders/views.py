from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order, Product
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags




@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.email = form.cleaned_data['email']
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                #reduce the number of items in inventory based on this sale
                item['product'].quantity = item['product'].quantity - item['quantity']
                item['product'].save()
            # clear the cart
            cart.clear()
            # set the order in the session
            request.session['order_id'] = order.id

            return render(request, 'orders/order/created.html', {'order_id':order.id})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


