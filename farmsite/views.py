from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Product,Contact,testimonial
from users.models import cart,wishList
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    product = Product.objects.all().filter(prime=True)
    test = testimonial.objects.all()
    if request.user.is_authenticated:
        cartObject = cart.objects.filter(user=request.user).values("productID")
        item = len(cartObject)
        if item==1:
            if cartObject[0].get('productID') == None:
                item=0
    else:
        item=0
    return render(request,'farmsite/home.html',{'products':product, 'testi': test,'item':item})


def shop(request):
    product = Product.objects.all()
    if request.user.is_authenticated:
        cartObject = cart.objects.filter(user=request.user).values("productID")
        item = len(cartObject)
        if item==1:
            if cartObject[0].get('productID') == None:
                item=0
    else:
        item=0
    return render(request,'farmsite/shop.html',{'products':product,'item':item})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mO = Contact.objects.create(name=name,email=email,message=message)
        mO.save()
    if request.user.is_authenticated:
        cartObject = cart.objects.filter(user=request.user).values("productID")
        item = len(cartObject)
        if item==1:
            if cartObject[0].get('productID') == None:
                item=0
    else:
        item=0
    return render(request,'farmsite/contacts.html',{'item':item})

def blog(request):
    return render(request,'farmsite/blog.html')

@login_required
def addCart(request,pk):
    productObject = Product.objects.get(id=pk)
    cartObject = cart.objects.get(user=request.user)
    cartObject.productID.add(productObject)
    cartObject.save()
    product = Product.objects.all()
    if request.user.is_authenticated:
        cartObject = cart.objects.filter(user=request.user).values("productID")
        item = len(cartObject)
        if item==1:
            if cartObject[0].get('productID') == None:
                item=0
    else:
        item=0
    return render(request,'farmsite/shop.html',{'products':product,'item':item})


@login_required
def addWish(request,pk):
    productObject = Product.objects.get(id=pk)
    cartObject = wishList.objects.get(user=request.user)
    cartObject.productID.add(productObject)
    cartObject.save()
    product = Product.objects.all()
    if request.user.is_authenticated:
        cartObject = cart.objects.filter(user=request.user).values("productID")
        item = len(cartObject)
        if item==1:
            if cartObject[0].get('productID') == None:
                item=0
    else:
        item=0
    return render(request,'farmsite/shop.html',{'products':product,'item':item})

@login_required
def cartPage(request):
    cartObject = cart.objects.filter(user=request.user).values("productID")
    myList = []
    try:
        for data in cartObject:
            id = data['productID']
            myList.append(Product.objects.get(id=id))
    except:
        pass
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
    cartObject = cart.objects.filter(user=request.user).values("productID")
    print(cartObject)
    item = len(cartObject)
    if item==1:
        if cartObject[0].get('productID') == None:
            item=0
    return render(request,'farmsite/cart.html',{'items': myList,'price':price,'discount':discount,'total':total,'item':item})

@login_required
def removeItem(request,pk):
    cartObject = cart.objects.get(user=request.user)
    cartObject.productID.remove(Product.objects.get(id=pk))
    cartObject = cart.objects.filter(user=request.user).values("productID")
    myList = []
    try:
        for data in cartObject:
            id = data['productID']
            myList.append(Product.objects.get(id=id))
    except:
        pass
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
    cartObject = cart.objects.filter(user=request.user).values("productID")
    item = len(cartObject)
    if item==1:
        if cartObject[0].get('productID') == None:
            item=0
    return render(request,'farmsite/cart.html',{'items': myList,'price':price,'discount':discount,'total':total,'item':item})


@login_required
def editWish(request,pk):
    cartObject = wishList.objects.get(user=request.user)
    cartObject.productID.remove(Product.objects.get(id=pk))
    cartObject = wishList.objects.filter(user=request.user).values("productID")
    myList = []
    try:
        for data in cartObject:
            id = data['productID']
            myList.append(Product.objects.get(id=id))
    except:
        pass
    cartObject = cart.objects.filter(user=request.user).values("productID")
    print(cartObject)
    item = len(cartObject)
    if item==1:
        if cartObject[0].get('productID') == None:
            item=0
    return render(request,'farmsite/wishlist.html',{'item':item,'items':myList})


def mywishlist(request):
    cartObject = wishList.objects.filter(user=request.user).values("productID")
    myList = []
    try:
        for data in cartObject:
            id = data['productID']
            myList.append(Product.objects.get(id=id))
    except:
        pass
    cartObject = cart.objects.filter(user=request.user).values("productID")
    print(cartObject)
    item = len(cartObject)
    if item==1:
        if cartObject[0].get('productID') == None:
            item=0
    return render(request,'farmsite/wishlist.html',{'item':item,'items':myList})

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'farmsite/product.html',{'product':product})