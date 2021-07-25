from django import http
from django.http.response import Http404
from eshop_product.models import Product
from django.shortcuts import redirect, render
from .forms import UserNewOrderForm
from . models import Order, OrderDetail
from eshop_product.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():

        order = Order.objects.filter(owner_id = request.user.id, is_paid = False).first()
        if order is None:
            order = Order.objects.create(owner_id = request.user.id, is_paid = False)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id = product_id)

        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        #todo: redirect user to user panel
        # return redirect('/')
        return redirect(f'/product/{product.id}/{product.title.replace(" ", "-")}')

    return redirect('/')

@login_required(login_url='/login') 
def user_open_order(request):
    context= {
        'order': None,
        'details' : None,
        'total_price' : None,
        'taxation' : None,
        'total_price_with_taxation' : None
    }
    
    open_order:Order = Order.objects.filter(owner_id = request.user.id, is_paid = False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()

    total_price = 0
    for detail in open_order.orderdetail_set.all():
        total_price = total_price + (detail.product.price * detail.count)
    taxation = int(total_price * (9/100))
    total_price_with_taxation = int(total_price - taxation)
    context['taxation'] = taxation
    context['total_price_with_taxation'] = total_price_with_taxation
    context['total_price'] = total_price
    return render(request, 'order/user_open_order.html', context)


@login_required(login_url='/login') 
def remove_oreder_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id = detail_id, order__owner_id = request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/open-order')
    raise Http404()


   