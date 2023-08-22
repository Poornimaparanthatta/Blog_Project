from django.shortcuts import render,redirect
from backend.models import CategoryDB,BlogDB
from frontend.models import UserCategoryDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def Cat_add(request):
    return render(request,"Add_Category.html")

def Cat_save(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        de=request.POST.get('description')
        im=request.FILES['image']
        obj=CategoryDB(Category=ca,Description=de,Image=im)
        obj.save()
        return redirect(Cat_add)

def Cat_dis(request):
    data=CategoryDB.objects.all()
    return render(request,"Display_Category.html",{'data':data})

def Cat_edit(request,dataid):
    data=CategoryDB.objects.get(id=dataid)
    return render(request,"Edit_Category.html",{'data':data})

def Cat_update(request,dataid):
    if request.method=="POST":
        ca = request.POST.get('category')
        de = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(Category=ca,Description=de,Image=file)
        return redirect(Cat_dis)

def Cat_del(request,dataid):
    data=CategoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(Cat_dis)

def Blog_add(request):
    data=CategoryDB.objects.all()
    return render(request,"Add_Blog.html",{'data':data})

def Blog_save(request):
    if request.method=="POST":
        cna=request.POST.get('category')
        bna=request.POST.get('blog')
        da=request.POST.get('date')
        au=request.POST.get('author')
        ci=request.POST.get('city')
        co=request.POST.get('content')
        bim=request.FILES['bimage']
        obj=BlogDB(Category=cna,Blog_Title=bna,Date=da,Author=au,Blog_Image=bim,City=ci,Content=co)
        obj.save()
        return redirect(Blog_add)
def Blog_dis(request):
    data=BlogDB.objects.all()
    return render(request,"Display_blogs.html",{'data':data})

def Blog_edit(req,dataid):
    data=CategoryDB.objects.all()
    products=BlogDB.objects.get(id=dataid)
    return render(req,"Edit_Blog.html",{'data':data,'products':products})

def Blog_Update(request,dataid):
    if request.method=="POST":
        cna=request.POST.get('category')
        bna=request.POST.get('blog')
        da=request.POST.get('date')
        au=request.POST.get('author')
        ci=request.POST.get('city')
        co=request.POST.get('content')
        try:
            img = request.FILES['bimage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = BlogDB.objects.get(id=dataid).Image
        BlogDB.objects.filter(id=dataid).update(Category=cna,Blog_Title=bna,Date=da,Author=au,Blog_Image=file,City=ci,Content=co)
        return redirect(Blog_dis)

def Blog_delete(request,dataid):
    data=BlogDB.objects.filter(id=dataid)
    data.delete()
    return redirect(Blog_dis)

def adminloginpage(request):
   return render(request,"AdminLogin.html")

def adminlogin(request):
    if request.method=="POST":
        username_b=request.POST.get('name')
        password_b=request.POST.get('word')
        if User.objects.filter(username__contains=username_b).exists():
            user=authenticate(username=username_b,password=password_b)
            if user is not None:
                login(request,user)
                request.session['username'] = username_b
                request.session['password'] = password_b

                return redirect(indexpage)
            else:
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)


def usercatpage(request):
    return render(request,"User_Cat.html")

def Catsave(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        de=request.POST.get('description')
        im=request.FILES['image']
        obj=UserCategoryDB(Category=ca,Description=de,Image=im)
        obj.save()
        return redirect(usercatpage)

