from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Product,Contact,testimonial
from users.models import cart
# Create your views here.

def index(request):
    product = Product.objects.all().filter(prime=True)
    test = testimonial.objects.all()
    return render(request,'farmsite/home.html',{'products':product, 'testi': test})

def shop(request):
    product = Product.objects.all()
    return render(request,'farmsite/shop.html',{'products':product})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mO = Contact.objects.create(name=name,email=email,message=message)
        mO.save()
    return render(request,'farmsite/contacts.html')

def blog(request):
    return render(request,'farmsite/blog.html')

def addCart(request,pk):
    productObject = Product.objects.get(id=pk)
    cartObject = cart.objects.get(user=request.user)
    cartObject.productID.add(productObject)
    cartObject.save()
    product = Product.objects.all()
    return render(request,'farmsite/shop.html',{'products':product})

def cartPage(request):
    cartObject = cart.objects.filter(user=request.user).values("productID")
    myList = []
    for data in cartObject:
        id = data['productID']
        myList.append(Product.objects.get(id=id))
    price = 0
    for data in myList:
        price+=data.price
    discount =0
    for data in myList:
        op = data.price
        dc = data.discount
        discount += op*(dc/100.0)
    print(discount)
    total = (price+50)-discount
    return render(request,'farmsite/cart.html',{'items': myList,'price':price,'discount':discount,'total':total})