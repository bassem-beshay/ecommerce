from django.shortcuts import render , redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# # Create your views here.

def index(request):
    cat = Category.objects.all()
    cart = request.session.get('cart', {})
    cart_count = len(cart) 
    context = {'cat': cat, 'cart_count': cart_count}
    return render(request, 'client/index.html' , context)


def product(request, category_id):
    if "user_id" not in request.session:
        return redirect("login")
    categorye = get_object_or_404(Category ,category_id=category_id)  
    prod = Product.objects.filter(category_id=categorye) 
    context = { 'prod': prod}
    return render(request, 'client/products.html', context)


def product_detail(request, product_id):
    if "user_id" not in request.session:
        return redirect("login")
    pero = get_object_or_404(Product, product_id=product_id)
    cat = Product.objects.filter(category=pero.category).exclude(product_id=product_id)
    prode = Product.objects.filter(product_id=product_id)
    produce = get_object_or_404(Product, product_id=product_id)

    pcolors = ProductColor.objects.filter(product=produce)
    
    # تعيين color بقيمة افتراضية
    color = None  
    if pcolors.exists():
        color_ids = pcolors.values_list('color_id', flat=True) 
        color = Color.objects.filter(color_id__in=color_ids)  

    context = {'color': color, 'prode': prode, 'cat': cat}
    return render(request, 'client/product_details.html', context)






def cart(request, product_id):
  
    product = get_object_or_404(Product, product_id=product_id)

   
    cart = request.session.get('cart', {})

  
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1 
    else:
        cart[str(product_id)] = {
            'product_id': product.product_id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
            'img': product.img.url if product.img else None,  }
         

  
    request.session['cart'] = cart
    request.session.modified = True  

    return redirect('cart_view')  


def update_cart_quantity(request, product_id, action):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if action == "increase":
            cart[str(product_id)]['quantity'] += 1
        elif action == "decrease" and cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1

    request.session['cart'] = cart
    request.session.modified = True

    total_price = sum(item['quantity'] * item['price'] for item in cart.values())

    return JsonResponse({
        'success': True,
        'quantity': cart[str(product_id)]['quantity'],
        'total_price': total_price
    })



def cart_view(request):
    if "user_id" not in request.session:
        return redirect("login")
    cart = request.session.get('cart', {})  
    return render(request, 'client/cart.html', {'cart': cart})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    request.session.modified = True  

    return redirect('cart_view')

def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('cart_view')



def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('user')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        Client.objects.create(user_name =fname, password=password , email=email, phone=phone, address=address)
        return redirect('login')
    return render(request, 'client/signup.html')

def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')

        try:
            client = Client.objects.get(user_name=user, password=password)
            request.session['user_id'] = client.user_id  # تخزين ID المستخدم في الجلسة
            request.session.modified = True  # تأكيد حفظ الجلسة
            return redirect('profile')  # الانتقال إلى صفحة البروفايل بعد تسجيل الدخول
        except Client.DoesNotExist:
            return render(request, 'client/login.html', {'error': 'Invalid username or password'})

    return render(request, 'client/login.html')

def profile(request):
    user_id = request.session.get('user_id')  # جلب `user_id` من الجلسة

    if not user_id:
        return redirect('login')  # إعادة التوجيه إلى تسجيل الدخول إذا لم يكن هناك `user_id` في الجلسة

    try:
        user = Client.objects.get(user_id=user_id)  # جلب بيانات المستخدم من قاعدة البيانات
        cat = Category.objects.all()
        cart = request.session.get('cart', {})
        cart_count = len(cart)
        context = {'cat': cat, 'cart_count': cart_count, 'user': user}
        return render(request, 'client/navpro.html', context)
    except Client.DoesNotExist:
        return redirect('login') 



def logout(request):
    request.session.flush()
    return redirect('/login')