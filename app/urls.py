from django.urls import path
from app import views

urlpatterns = [
    # tvs
    path('api_products/', views.api_products, name='apiProducts' ),
    path('api_categories/', views.api_categories, name='apiCategories' ),
    path('getProductDetails/<int:product_id>/', views.getProductDetails, name='getProductDetails' ),
    path('api_categoryproducts/<int:category_id>/', views.getProductsByCategory, name='apiCategoryproducts' ),

    # phones
    path('api_phones/', views.api_phones, name='apiPhones' ),
    path('api_phone_categories/', views.api_phone_categories, name='apiPhoneCategories' ),
    path('getPhoneDetails/<int:phone_id>/', views.getPhoneDetails, name='getPhoneDetails' ),
    path('api_categoryphones/<int:phonecategory_id>/', views.getPhonesByPhoneCategory, name='apiCategoryphones' ),

    # fridges 
    path('api_fridges/', views.api_fridges, name='apiFridges' ),
    path('api_fridge_categories/', views.api_fridge_categories, name='apiFridgeCategories' ),
    path('getFridgeDetails/<int:fridge_id>/', views.getFridgeDetails, name='getFridgeDetails' ),
    path('api_categoryfridges/<int:fridgecategory_id>/', views.getFridgesByFridgeCategory, name='apiCategoryfridges' ),

    # home appliances 
    path('api_homeAppliances/', views.api_homeAppliances, name='apiHomeAppliances' ),
    path('api_homeAppliances_categories/', views.api_homeAppliances_categories, name='apiHomeAppliancesCategories' ),
    path('getHomeAppliancesDetails/<int:homeAppliances_id>/', views.getHomeAppliancesDetails, name='getHomeAppliancesDetails' ),
    path('api_categoryhomeAppliances/<int:homeAppliancescategory_id>/', views.getHomeAppliancesByHomeAppliancesCategory, name='apiCategoryhomeAppliances' ),
]