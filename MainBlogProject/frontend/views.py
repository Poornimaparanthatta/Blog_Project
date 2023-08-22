from django.shortcuts import render,redirect
from backend.models import CategoryDB,BlogDB
from frontend.models import UserBlogDB,UserCategoryDB,UserRegDB,contactDB,newsDB,commentdb,blogsdb
from django.contrib import messages


# Create your views here.

def homepage(req):
    data=CategoryDB.objects.all()
    return render(req,"Home.html",{'data':data})

def contactpage(req):
    return render(req,"Contact.html")

def aboutpage(req):
    return render(req,"About.html")

def blogspage(req,catg):
    blogs=BlogDB.objects.filter(Category=catg)
    return render(req,"Blogs.html",{'blogs':blogs})

def singleblog(req,dataid):
    data=BlogDB.objects.get(id=dataid)
    return render(req,"Single_Blog.html",{'data':data})



def usercatdisp(request):
    data=UserCategoryDB.objects.all()
    return render(request,"User_Category.html",{'data':data})

def addblogpage(req):
    data=UserCategoryDB.objects.all()
    return render(req,"Add_Blogs.html",{'data':data})

def userblogsave(request):
    if request.method=="POST":
        cna=request.POST.get('cat')
        bna=request.POST.get('blog')
        da=request.POST.get('date')
        au=request.POST.get('author')
        ci=request.POST.get('city')
        co=request.POST.get('content')
        bim=request.FILES['bimage']
        obj=UserBlogDB(Category=cna,Blog_Title=bna,Date=da,Author=au,Blog_Image=bim,City=ci,Content=co)
        obj.save()
        messages.success(request,"Blog Posted")
        return redirect(addblogpage)

def userblogdis(request,catb):
    data=UserBlogDB.objects.filter(Category=catb)
    return render(request,"User_blogs.html",{'data':data})

def usersingleblog(req,dataid):
    data=UserBlogDB.objects.get(id=dataid)
    comments=commentdb.objects.filter(blog=dataid)
    return render(req,"UserSingleBlog.html",{'data':data, 'comments':comments} )

def userloginpage(req):
    return render(req,"UserloginPage.html")

def user_reg(request):
    if request.method=="POST":
        em=request.POST.get('email')
        un=request.POST.get('username')
        pa=request.POST.get('password')
        obj3=UserRegDB(Username=un,Email=em,Password=pa)
        obj3.save()
        return redirect(userloginpage)

def userlogin(request):
    if request.method=="POST":
        username_b=request.POST.get('username')
        password_b=request.POST.get('password')
        if UserRegDB.objects.filter(Username=username_b,Password=password_b).exists():

            request.session['usernamep']=username_b
            request.session['passwordp']=password_b

            return redirect(homepage)
        else:
            return redirect(userloginpage)
        return redirect(userloginpage)

def userlogout(request):
    del request.session['usernamep']
    del request.session['passwordp']
    return redirect(userloginpage)

def savecontactpage(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        me=req.POST.get('message')
        obj=contactDB(Name=na,Email=em,Message=me)
        obj.save()
        messages.success(req,"Message Sent")
        return redirect(contactpage)

def savenewsletter(req):
    if req.method=="POST":
        fn=req.POST.get('fullname')
        ma=req.POST.get('emaddress')
        obj=newsDB(Fullname=fn,Eaddress=ma)
        obj.save()
        return redirect(homepage)

def search(req):
    if req.method=="POST":
        query=req.POST.get('qry')
        if query:
            results=CategoryDB.objects.filter(Category__contains=query)
        else:
            results=[]
        return render(req, 'search.html',{'results':results})

def comment(req,postid):
    if req.method == "POST":
        cm = req.POST.get("comment")
        # em= req.POST.get("mail")
        # na= req.POST.get("name")
        post=UserBlogDB.objects.get(id=postid).id
        obj = commentdb(blog=post, Comment=cm)
        obj.save()
        return redirect(usersingleblog,postid)

def comment1(req,postid):
    if req.method == "POST":
        cm = req.POST.get("comment")
        em= req.POST.get("mail")
        na= req.POST.get("name")
        post=BlogDB.objects.get(id=postid).id
        obj = commentdb(blog=post, Name=na, Comment=cm,Email=em)
        obj.save()
        return redirect(singleblog,postid)


def subscription(req):
    return render(req,"subscriptionn.html")

def cart(req):
    return render(req,"cart.html")