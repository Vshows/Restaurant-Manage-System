from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('menu_list/<str:name>',views.menu_list,name='menu_list'),
    path('detail/<str:name>/',views.detail,name='deatil'),
    path('login/',views.login,name='login'),

    path('cart/add',views.cart_add,name='cart_add'),
    path('cart',views.cart,name='cart'),
    path('bill/',views.bill_create,name='bill'),
    path('cancel/',views.cancel,name='cancel'),
    path('user_check/',views.user_check,name = 'user_check'),
    path('evaluate/',views.evaluate,name='evaluate'),
    path('user_add/',views.user_add,name='user_add'),
    path('logout/',views.logout,name='logout'),
    path('edit/',views.edit,name='edit'),
    path('edit_solve/',views.edit_solve,name='edit_solve')
]
