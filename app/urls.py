from django.urls import path
from app import views

urlpatterns = [
    path('api_products/', views.api_products, name='apiProducts' ),
    path('api_categories/', views.api_categories, name='apiCategories' ),
    path('getProductDetails/<int:product_id>/', views.getProductDetails, name='getProductDetails' ),
    path('api_categoryproducts/<int:category_id>/', views.getProductsByCategory, name='apiCategoryproducts' ),
    path('api_phones/', views.api_phones, name='apiPhones' ),
    path('api_phone_categories/', views.api_phone_categories, name='apiPhoneCategories' ),
    path('getPhoneDetails/<int:phone_id>/', views.getPhoneDetails, name='getPhoneDetails' ),
    path('api_categoryphones/<int:phonecategory_id>/', views.getPhonesByPhoneCategory, name='apiCategoryphones' ),
]