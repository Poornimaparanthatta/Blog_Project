from django.urls import path
from frontend import views


urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('blogspage/<catg>/',views.blogspage,name="blogspage"),
    path('singleblog/<int:dataid>/', views.singleblog, name="singleblog"),
    path('addblogpage/', views.addblogpage, name="addblogpage"),
    path('usercatdisp/', views.usercatdisp, name="usercatdisp"),
    path('userblogsave/', views.userblogsave, name="userblogsave"),
    path('userblogdis/<catb>/', views.userblogdis, name="userblogdis"),
    path('usersingleblog/<int:dataid>/', views.usersingleblog, name="usersingleblog"),
    path('comment/<int:postid>/', views.comment, name="comment"),
    path('comment1/<int:postid>/', views.comment1, name="comment1"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('user_reg/', views.user_reg, name="user_reg"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('savecontactpage/', views.savecontactpage, name="savecontactpage"),
    path('savenewsletter/', views.savenewsletter, name="savenewsletter"),
    path('search/', views.search, name="search"),
    path('subscription/', views.subscription, name="subscription"),
    path('cart/', views.cart, name="cart")


]