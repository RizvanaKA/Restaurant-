"""
URL configuration for Restuarant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.login_page),
    path('admin_add_table/',views.admin_add_table),
    path('admin_view_table/',views.admin_view_table),
    path('admin_edit_table/<id>',views.admin_edit_table),
    path('admin_add_food/',views.admin_add_food),
    path('admin_view_food/',views.admin_view_food),
    path('admin_edit_food/<id>',views.admin_edit_food),
    path('admin_view_booking/',views.admin_view_booking),
    path('admin_view_order/',views.admin_view_order),
    path('view_food_feedback/',views.view_food_feedback),
    path('user_logout/',views.user_logout),
    path('admin_order_sub/<id>',views.admin_order_sub),
    path('user_add_date/<id>',views.user_add_date),
    path('admin_update_order/<id>',views.admin_update_order),
    path('admin_home/',views.admin_home),
    path('admin_view_feedbacks/',views.admin_view_feedbacks),
    path('login_post/',views.login_post),
    path('add_table_post/',views.add_table_post),
    path('edit_table_post/',views.edit_table_post),
    path('delete_table/<id>',views.delete_table),
    path('delete_food/<id>',views.delete_food),
    path('add_food_post/',views.add_food_post),
    path('edit_food_post/',views.edit_food_post),
    path('order_update_post/',views.order_update_post),
    path('user_reg_post/',views.user_reg_post),
    path('user_reg/',views.user_reg),
    path('user_home/',views.user_home),
    path('book_table_post/',views.book_table_post),
    path('user_view_book/',views.user_view_book),
    path('user_send_feedback/',views.user_send_feedback),
    path('send_feedback_post/',views.send_feedback_post),
    path('user_view_food/',views.user_view_food),
    path('user_view_order/',views.user_view_order),
    path('food_rate_post/',views.food_rate_post),
    path('user_add_food_rating/<id>',views.user_add_food_rating),
    path('add_cart/<id>',views.add_cart),
    path('user_view_cart2/',views.user_view_cart2),
    path('user_view_food_rating/<id>',views.user_view_food_rating),
    path('delete_feedback/<id>',views.delete_feedback),
    path('remove_cart_item/<sub_id>/', views.remove_cart_item),
    path('update_booking_status/<id>/', views.update_booking_status),

    # urls.py
    path('raz_pay/<str:amount>/<int:id>/', views.raz_pay, name='raz_pay'),

    path('user_view_table/',views.user_view_table),
    path('user_book_table/',views.user_book_table),
    path('cancel_booking/<id>',views.cancel_booking),
    path('cancel_order/<id>',views.cancel_order),
    path('raz_pay/<id>/<amount>/',views.raz_pay),
    path('payment_success/',views.payment_success),


]
