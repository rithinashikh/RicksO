from django.urls import path
from . import views
from .views import UserLoginView, UserSignupView, AdminLoginView, AdminAddProductView, AdminAddCategoryView
from .views import UpdateCategoryView,UserOTPLoginView, OrderUpdateView, EditUserProfileView, ChangePasswordView

urlpatterns = [

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('userlogin/', UserLoginView.as_view(), name='userlogin'),
    path('shop/', views.shop, name='shop'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('usersignup/', UserSignupView.as_view(), name='usersignup'),
    path('adminlogin/', AdminLoginView.as_view(), name='adminlogin'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('adminuserlist/', views.adminuserlist, name='adminuserlist'),
    path('adminproductlist/', views.adminproductlist, name='adminproductlist'),
    path('adminaddproduct/', AdminAddProductView.as_view(), name='adminaddproduct'),
    path('updateproduct/', views.updateproduct, name='updateproduct'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('userblock/', views.userblock, name='userblock'),
    path('deleteproduct/', views.deleteproduct, name='deleteproduct'),
    path('adminaddcategory/', AdminAddCategoryView.as_view(), name='adminaddcategory'),
    path('shopsingle/', views.shopsingle, name='shopsingle'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('admincategorylist/', views.admincategorylist, name='admincategorylist'),
    path('deletecategory/', views.deletecategory, name='deletecategory'),
    path('updatecategory/', UpdateCategoryView.as_view(), name='updatecategory'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('otplogin/', views.otplogin, name='otplogin'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderconfirm/', views.orderconfirm, name='orderconfirm'),
    path('delcartitems/', views.delcartitems, name='delcartitems'),
    path('updateaddress/<int:id>', views.updateaddress, name='updateaddress'),
    path('deleteaddress/', views.deleteaddress, name='deleteaddress'),
    path('address_select/', views.address_select, name='address_select'),
    path('order/', views.order, name='order'),
    path('plus_cart', views.plus_cart),
    path('minus_cart', views.minus_cart),
    path('cancelorder/<int:id>', views.cancelorder, name='cancelorder'),
    path('returnorder/<int:id>', views.returnorder, name='returnorder'),
    path('adminorderlist/', views.adminorderlist, name='adminorderlist'),
    path('updateorder/<int:id>', OrderUpdateView.as_view(), name='updateorder'),
    path('paypal/', views.paypal, name='paypal'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('edituserprofile/', EditUserProfileView.as_view(), name='edituserprofile'),
    path('changepassword/', ChangePasswordView.as_view(), name='changepassword'),
    path('userotplogin/', UserOTPLoginView.as_view(), name='userotplogin'),
    path('updateprofileaddress/<int:id>', views.updateprofileaddress, name='updateprofileaddress'),
    path('addprofileaddress/', views.addprofileaddress, name='addprofileaddress'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlistdelete/<int:id>', views.wishlistdelete, name='wishlistdelete'),
    path('sales_report/', views.sales_report, name='sales_report'),
    path('cancelcoupon/', views.cancelcoupon, name='cancelcoupon'),
    path('admincouponlist/', views.admincouponlist, name='admincouponlist'),
    path('adminaddcoupon/', views.adminaddcoupon, name='adminaddcoupon'),
    path('deletecoupon/', views.deletecoupon, name='deletecoupon'),
    path('updatecoupon/', views.updatecoupon, name='updatecoupon'),
    path('generateinvoice/', views.generateinvoice, name='generateinvoice'),
    path('updatebanner/', views.updatebanner, name='updatebanner'),
    path('adminaddbanner/', views.adminaddbanner, name='adminaddbanner'),
    path('adminbannerlist/', views.adminbannerlist, name='adminbannerlist'),
    path('deletebanner/', views.deletebanner, name='deletebanner'),
    # path('download/', views.download, name='download'),
]