from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime


from myapp.models import *


def login_page(request):
    return render(request,'login.html')

def login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    # print(request.POST)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # print(user,'kkkkkkkk')
        if user.groups.filter(name='admin').exists():
            # print('llll')
            login(request, user)
            messages.success(request,'logined Successfully..!!')
            return redirect('/myapp/admin_home/')
        elif user.groups.filter(name='user').exists():
            login(request,user)
            messages.success(request,'logined Successfully..!!')

            return redirect('/myapp/user_home/')
        else:
            return redirect('/myapp/')
    else:
        messages.warning(request, 'invalid username or password')
        return redirect('/myapp/')

@login_required(login_url='/myapp/')
def admin_add_table(request):
    return render(request,'admins/add table.html')


@login_required(login_url='/myapp/')

def add_table_post(request):
    tablename=request.POST['tablename']
    capacity=request.POST['capacity']

    obj=Table_table()
    obj.tablename=tablename
    obj.capacity=capacity
    obj.save()
    return redirect('/myapp/admin_view_table')


@login_required(login_url='/myapp/')

def admin_view_table(request):
    a=Table_table.objects.all()
    return render(request,'admins/view table.html',{'data':a})

def delete_table(request,id):
    a=Table_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/admin_view_table/')

@login_required(login_url='/myapp/')

def admin_edit_table(request,id):
    request.session['tid']=id
    a=Table_table.objects.get(id=id)
    return render(request,'admins/edit table.html',{"data":a})
def edit_table_post(request):
    tablename = request.POST['tablename']
    capacity = request.POST['capacity']

    obj = Table_table.objects.get(id=request.session['tid'])
    obj.tablename = tablename
    obj.capacity = capacity
    obj.save()
    return redirect('/myapp/admin_view_table')

@login_required(login_url='/myapp/')

def admin_add_food(request):
    return render(request,'admins/admin_add_food.html')
def add_food_post(request):
    food=request.POST['food']
    category=request.POST['category']
    price=request.POST['price']
    description=request.POST['description']
    qty=request.POST['qty']

    obj=Food_Items_table()
    obj.name=food
    obj.category=category
    obj.price=price
    obj.description=description
    obj.status='pending..'
    obj.quantity=qty
    obj.save()
    return redirect('/myapp/admin_view_food/')

@login_required(login_url='/myapp/')

def admin_view_food(request):
    a=Food_Items_table.objects.all()
    return render(request,'admins/admin_view_food.html',{'data':a})
def delete_food(request,id):
    a=Food_Items_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/admin_view_food/')


@login_required(login_url='/myapp/')

def admin_edit_food(request,id):
    request.session['fid']=id
    a=Food_Items_table.objects.get(id=id)
    return render(request,'admins/admin_edit_food.html',{"data":a})

def edit_food_post(request):
    food=request.POST['food']
    category=request.POST['category']
    price=request.POST['price']
    description=request.POST['description']
    qty=request.POST['qty']

    obj=Food_Items_table(id=request.session['fid'])
    obj.name=food
    obj.category=category
    obj.price=price
    obj.description=description
    obj.status='pending..'
    obj.quantity=qty
    obj.save()
    return redirect('/myapp/admin_view_food/')

@login_required(login_url='/myapp/')

def admin_view_booking(request):
    a=Booking_table.objects.all()
    return render(request,'admins/admin_view_booking.html',{'data':a})

@login_required(login_url='/myapp/')

def update_booking_status(request,id):
    a=Booking_table.objects.get(id=id)
    a.status='Completed'
    a.save()
    return redirect("/myapp/admin_view_booking/#block")
@login_required(login_url='/myapp/')

def admin_view_order(request):
    a=Order_main_table.objects.filter(status='paid')
    return render(request,'admins/admin_view_order.html',{'data':a})


@login_required(login_url='/myapp/')

def admin_order_sub(request,id):
    a=Order_sub_table.objects.filter(ORDERMAIN__id=id)
    ab=Order_main_table.objects.get(id=id)
    return render(request,'admins/order_sub.html',{'data':a,"total":ab.amount})


@login_required(login_url='/myapp/')

def admin_update_order(request,id):
    request.session['rid']=id
    return render(request,'admins/update order.html')
def order_update_post(request):
    status=request.POST['status']
    Order_main_table.objects.filter(id=request.session['rid']).update(status=status)
    return redirect('/myapp/admin_view_order/')


@login_required(login_url='/myapp/')

def admin_home(request):
    return render(request,'admins/index.html')
def admin_view_feedbacks(request):
    a=Feedback_table.objects.all()
    return render(request,'admins/admin_view_feedback.html',{'data':a})


#######################user#######################

def user_reg(request):
    return render(request,'user/user_reg_index.html')
def user_reg_post(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    address=request.POST['address']
    pin=request.POST['pin']
    post=request.POST['post']
    username=request.POST['username']
    password=request.POST['password']

    user=User.objects.create(username=username, password=make_password(password),first_name=name,email=email)
    user.groups.add(Group.objects.get(name='user'))


    obj=User_table()
    obj.name=name
    obj.email=email
    obj.address=address
    obj.pin=pin
    obj.post=post
    obj.phone=phone
    obj.LOGIN=user
    obj.save()

    return redirect('/myapp/')
@login_required(login_url='/myapp/')

def user_home(request):
    return render(request,'user/user_index.html')

def book_table_post(request):
    tab=request.POST['tab']

    obj=Booking_table()
    obj.date=datetime.now()
    obj.status='booked'
    obj.USER=User_table.objects.get(LOGIN__id=request.user.id)
    obj.TABLE_id=tab
    obj.save()
    return redirect('/myapp/user_view_book/')


@login_required(login_url='/myapp/')

def user_view_book(request):
    a = Booking_table.objects.filter(USER__LOGIN_id=request.user.id).select_related('TABLE').order_by('-date')
    return render(request,'user/view_booking.html',{'data':a})
def cancel_booking(request,id):
    a=Booking_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/user_view_book/#block')


@login_required(login_url='/myapp/')

def user_view_table(request):
    a=Table_table.objects.all()
    return render(request,'user/view table.html',{'data':a})

@login_required(login_url='/myapp/')


def user_add_date(request,id):
    request.session['did']=id
    return render(request,'user/add date.html',{'id':id})

def user_book_table(request):
    bookdate= request.POST['Date']
    date=datetime.now().today().date()
    var=Booking_table.objects.filter(TABLE_id=request.session['did'],date=date)
    if var.exists():
        messages.warning(request,'Already Booked')
        return redirect('/myapp/user_view_table/#block')

    var2=Booking_table()
    var2.date=date
    var2.bookingdate=bookdate
    var2.TABLE=Table_table.objects.get(id=request.session['did'])
    var2.USER=User_table.objects.get(LOGIN_id=request.user.id)
    var2.status='Booked'
    var2.save()
    messages.success(request, f'{var2.TABLE.tablename} Booking success')

    return redirect('/myapp/user_view_table/#block')



@login_required(login_url='/myapp/')

def user_send_feedback(request):
    return render(request,'user/user_send_feedback.html')
def send_feedback_post(request):
    feed=request.POST['feedback']

    obj=Feedback_table()
    obj.feedback=feed
    obj.date=datetime.now()
    obj.USER=User_table.objects.get(LOGIN_id=request.user.id)
    obj.save()
    messages.success(request, "Feedback sent successfully!")
    return redirect('/myapp/user_home/')


def view_food_feedback(request):
    ab=Review_table.objects.all()
    return render(request,'admins/view_feedback.html',{'data':ab})


@login_required(login_url='/myapp/')
def user_view_food(request):
    a=Food_Items_table.objects.all()


    return render(request,'user/view food.html',{"data":a})





@login_required(login_url='/myapp/')

def user_view_order(request):
    orders = Order_main_table.objects.filter(USER__LOGIN_id=request.user.id,status='paid')

    order_list = []
    total_amount_all_orders = 0
    order_ids = []

    for order in orders:
        items = Order_sub_table.objects.filter(ORDERMAIN=order)
        order_list.append({
            'order': order,
            'items': items
        })
        total_amount_all_orders += order.amount
        order_ids.append(str(order.id))

    return render(request, 'user/view orders.html', {
        'orders': order_list,
        'total_amount_all_orders': total_amount_all_orders,
        'order_ids': ','.join(order_ids),
    })


def cancel_order(request,id):
    a=Order_main_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/user_view_order/')





from django.db.models import F

def add_cart(request, id):
    if request.method != "POST":
        messages.error(request, "Invalid request method.")
        return redirect('/myapp/user_view_food/')

    try:
        qty = int(request.POST.get('qty', 1))
    except (ValueError, TypeError):
        messages.error(request, "Invalid quantity.")
        return redirect('/myapp/user_view_food/')

    if qty < 1:
        messages.error(request, "Quantity must be at least 1.")
        return redirect('/myapp/user_view_food/')

    food = get_object_or_404(Food_Items_table, id=id)

    if food.quantity < qty:
        messages.warning(request, f"Only {food.quantity} unit(s) available. You requested {qty}.")
        return redirect('/myapp/user_view_food/')

    updated = Food_Items_table.objects.filter(id=food.id, quantity__gte=qty).update(quantity=F('quantity') - qty)
    if updated == 0:
        messages.warning(request, f"Only {food.quantity} unit(s) available. You requested {qty}.")
        return redirect('/myapp/user_view_food/')

    user = get_object_or_404(User_table, LOGIN_id=request.user.id)
    added_amount = qty * float(food.price)

    cart_main, _ = Order_main_table.objects.get_or_create(
        USER=user,
        status='cart',
        defaults={'amount': 0.0, 'quantity': 0}
    )

    sub = Order_sub_table.objects.filter(ORDERMAIN=cart_main, FOOD=food).first()
    if sub:
        sub.quantity += qty
        sub.amount += added_amount
        sub.save()
    else:
        sub = Order_sub_table.objects.create(
            ORDERMAIN=cart_main,
            FOOD=food,
            quantity=qty,
            amount=added_amount
        )

    totals = Order_sub_table.objects.filter(ORDERMAIN=cart_main).aggregate(
        total_qty=Sum('quantity'),
        total_amt=Sum('amount')
    )
    total_qty = int(totals['total_qty'] or 0)
    total_amt = float(totals['total_amt'] or 0.0)

    Order_main_table.objects.filter(id=cart_main.id).update(amount=total_amt, quantity=total_qty)

    cart_row = Cart_table.objects.filter(ORDERSUB__ORDERMAIN=cart_main, status='cart').first()
    if cart_row:
        cart_row.total_amount = total_amt
        cart_row.date = timezone.now().date()
        cart_row.save()
    else:
        Cart_table.objects.create(
            ORDERSUB=sub,
            status='cart',
            total_amount=total_amt,
            date=timezone.now().date()
        )

    messages.success(
        request,
        f"Added {qty} × {food.name} to cart. Cart now has {total_qty} item(s), total ₹{total_amt:.2f}."
    )
    return redirect('/myapp/user_view_cart2/#block')






@login_required(login_url='/myapp/')
def user_view_cart2(request):
    user = get_object_or_404(User_table, LOGIN_id=request.user.id)
    cart_main = Order_main_table.objects.filter(USER=user, status='cart').first()

    if not cart_main:
        return render(request, 'user/view_cart.html', {'subs': [], 'cart_main': None})

    subs = Order_sub_table.objects.filter(ORDERMAIN=cart_main).select_related('FOOD')
    return render(request, 'user/view_cart.html', {'subs': subs, 'cart_main': cart_main})



from django.db.models import Sum

@login_required(login_url='/myapp/')

def remove_cart_item(request, sub_id):
    if request.method != 'POST':
        messages.error(request, "Invalid request method.")
        return redirect('/myapp/user_view_cart2/#block')

    sub = get_object_or_404(Order_sub_table.objects.select_related('ORDERMAIN', 'FOOD'), id=sub_id)
    order_main = sub.ORDERMAIN
    food_item = sub.FOOD

    food_item.quantity = F('quantity') + sub.quantity
    food_item.save()

    sub.delete()

    totals = Order_sub_table.objects.filter(ORDERMAIN=order_main).aggregate(
        total_qty=Sum('quantity'),
        total_amt=Sum('amount')
    )
    total_qty = int(totals['total_qty'] or 0)
    total_amt = float(totals['total_amt'] or 0.0)

    if total_qty == 0:
        Cart_table.objects.filter(ORDERSUB__ORDERMAIN=order_main).delete()
        order_main.delete()
    else:
        order_main.amount = total_amt
        order_main.quantity = total_qty
        order_main.save(update_fields=['amount', 'quantity'])

        Cart_table.objects.filter(ORDERSUB__ORDERMAIN=order_main, status='cart').delete()
        rep_sub = Order_sub_table.objects.filter(ORDERMAIN=order_main).order_by('id').first()
        if rep_sub:
            Cart_table.objects.create(
                ORDERSUB=rep_sub,
                status='cart',
                total_amount=total_amt,
                date=timezone.now().date()
            )

    messages.success(request, "Item removed from cart and stock restored.")
    return redirect('/myapp/user_view_cart2/#block')



def user_view_food_rating(request,id):
    request.session['fid']=id
    a=Review_table.objects.filter(FOOD__id=id)
    return render(request,'user/view_food_ratings.html',{'data':a})

def delete_feedback(request,id):
    a=Review_table.objects.get(id=id)
    a.delete()
    return redirect("/myapp/user_view_food_rating/"+str(request.session['fid']))

def user_add_food_rating(request,id):
    request.session['rateid']=id
    return render(request,'user/feedback_rating.html')

def food_rate_post(request):
    rating=request.POST['rating']
    review=request.POST['feedback']


    obj=Review_table()
    obj.rating=rating
    obj.review=review
    obj.date=datetime.today()
    obj.USER=User_table.objects.get(LOGIN_id=request.user.id)
    obj.FOOD=Food_Items_table.objects.get(id=request.session['rateid'])
    obj.save()
    return redirect('/myapp/user_view_food_rating/')




# payment#######################################






@login_required(login_url='/myapp/')


def raz_pay(request, amount, id):
    from django.contrib import messages
    import razorpay

    try:
        amount = float(amount)
    except ValueError:
        messages.error(request, "Invalid amount.")
        return redirect('myapp/user_view_cart2/#block')

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"
    client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount_paise = int(round(amount * 100))

    order_data = {
        'amount': amount_paise,
        'currency': 'INR',
        'receipt': f'order_rcptid_{id}',
        'payment_capture': '1',
    }
    try:
        razorpay_order = client.order.create(data=order_data)
    except Exception:
        messages.error(request, "Failed to create Razorpay order. Try again.")
        return redirect('/myapp/user_view_cart2/#block')

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': amount_paise,
        'currency': 'INR',
        'order_id': razorpay_order['id'],
        'display_amount': amount,
        'order_main_id': id,
    }
    return render(request, 'user/pp.html', context)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import hmac, hashlib

@login_required(login_url='/myapp/')
@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        order_main_id = request.POST.get('order_main_id')

        # Verify signature
        secret = "MvUZ03MPzLq3lkvMneYECQsk"
        msg = f"{razorpay_order_id}|{razorpay_payment_id}"
        generated_signature = hmac.new(bytes(secret, 'utf-8'), bytes(msg, 'utf-8'), hashlib.sha256).hexdigest()

        if generated_signature == razorpay_signature:
            # Payment verified ✅
            order_main = get_object_or_404(Order_main_table, id=order_main_id)
            order_main.status = 'paid'
            order_main.save()

            # Reduce stock
            order_subs = Order_sub_table.objects.filter(ORDERMAIN=order_main)
            for sub in order_subs:
                food_item = sub.FOOD
                if food_item.quantity >= sub.quantity:
                    food_item.quantity -= sub.quantity
                else:
                    food_item.quantity = 0
                food_item.save()

            # Remove cart
            Cart_table.objects.filter(ORDERSUB__ORDERMAIN=order_main).delete()

            # Save payment
            Payment_table.objects.create(
                ORDER_id=order_main.id,
                date=datetime.now().strftime('%Y-%m-%d'),
                amount=order_main.amount,
                status='paid'
            )
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "failed", "msg": "Payment verification failed"})
    return JsonResponse({"status": "error", "msg": "Invalid request"})


def user_logout(request):
    logout(request)
    return redirect('/myapp/')