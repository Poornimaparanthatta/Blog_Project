from django.urls import path
from backend import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('Cat_add/',views.Cat_add,name="Cat_add"),
    path('Cat_save/',views.Cat_save,name="Cat_save"),
    path('Cat_dis/',views.Cat_dis,name="Cat_dis"),
    path('Cat_edit/<int:dataid>',views.Cat_edit,name="Cat_edit"),
    path('Cat_update/<int:dataid>',views.Cat_update,name="Cat_update"),
    path('Cat_del/<int:dataid>',views.Cat_del,name="Cat_del"),
    path('Blog_add/',views.Blog_add,name="Blog_add"),
    path('Blog_save/',views.Blog_save,name="Blog_save"),
    path('Blog_dis/',views.Blog_dis,name="Blog_dis"),
    path('Blog_edit/<int:dataid>',views.Blog_edit,name="Blog_edit"),
    path('Blog_Update/<int:dataid>',views.Blog_Update,name="Blog_Update"),
    path('Blog_delete/<int:dataid>',views.Blog_delete,name="Blog_delete"),
    path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('usercatpage/',views.usercatpage,name="usercatpage"),
    path('Catsave/',views.Catsave,name="Catsave")
]