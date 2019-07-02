from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/', views.index_Category, name='category'),
    url(r'^city/', views.index_City, name='city'),
    url(r'^goods/', views.index_Goods, name='goods'),
    url(r'^nearby/', views.index_Nearby, name='nearby'),
    url(r'^user/', views.index_login_Or_register, name='user'),
    url(r'^address/', views.index_showInfo, name='address'),
    url(r'^change/', views.change_Info_or_pwd, name='changeinfo'),
    url(r'^pay/', views.index_buy, name='pay'),
    url(r'^ordersCount/', views.orders_count, name='orderCount'),
    url(r'^walletCount/', views.wallet_count, name='walletCount'),
    url(r'^reviewCount/', views.reciew_count, name='reviewCount'),
    url(r'^commentPut/', views.commentPut, name='commentPut'),
    url(r'^commentGet/', views.commentGet, name='commentGet'),
    url(r'^show_orders/', views.show_orders, name='show_orders'),
    url(r'^show_review/', views.show_comments, name='show_comments'),
]