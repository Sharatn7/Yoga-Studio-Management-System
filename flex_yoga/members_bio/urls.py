from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/addrecord/', views.addrecord, name='addrecord'),
    path('search/display/', views.display, name='display'),
    path('search/display/<int:id>', views.display, name='display'),
    path('search/', views.search, name='search'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('payment/updatepay/<int:id>',
         views.update_payment, name='update_payment'),
    path('slotchange/<int:id>', views.slot, name='slot'),
    path('slotchange/updateslot/<int:id>',
         views.update_slot, name='update_slot'),
    path('test/', views.test, name='test'),
]
