from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['GET',])
def api_products(request):
    if request.method == "GET":
        products = Product.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = ProductSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def api_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getProductDetails(request, product_id):
    if request.method == "GET":
        product= Product.objects.filter(id = product_id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getProductsByCategory(request, category_id):
    if request.method == "GET":
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_phones(request):
    if request.method == "GET":
        phones = Phones.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(phones, request)

        # Serialize the result page
        serializer = PhoneSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_phone_categories(request):
    if request.method == "GET":
        phonecategories = PhoneCategory.objects.all()
        serializer = PhoneCategorySerializer(phonecategories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getPhoneDetails(request, phone_id):
    if request.method == "GET":
        phone= Phones.objects.filter(id = phone_id)
        serializer = PhoneSerializer(phone, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getPhonesByPhoneCategory(request, phonecategory_id):
    if request.method == "GET":
        phonecategory = get_object_or_404(PhoneCategory, id=phonecategory_id)
        phone = Phones.objects.filter(category=phonecategory)
        serializer = PhoneSerializer(phone, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_fridges(request):
    if request.method == "GET":
        fridge = Fridge.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(fridge, request)

        # Serialize the result page
        serializer = FridgeSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_fridge_categories(request):
    if request.method == "GET":
        fridgecategories = FridgeCategory.objects.all()
        serializer = FridgeCategorySerializer(fridgecategories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getFridgeDetails(request, fridge_id):
    if request.method == "GET":
        fridge= Fridge.objects.filter(id = fridge_id)
        serializer = FridgeSerializer(fridge, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getFridgesByFridgeCategory(request, fridgecategory_id):
    if request.method == "GET":
        fridgecategory = get_object_or_404(FridgeCategory, id=fridgecategory_id)
        fridge = Fridge.objects.filter(category=fridgecategory)
        serializer = FridgeSerializer(fridge, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET',])
def api_homeAppliances(request):
    if request.method == "GET":
        homeAppliances = HomeAppliances.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(homeAppliances, request)

        # Serialize the result page
        serializer = HomeAppliancesSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_homeAppliances_categories(request):
    if request.method == "GET":
        homeAppliancescategories = HomeAppliancesCategory.objects.all()
        serializer = HomeAppliancesCategorySerializer(homeAppliancescategories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getHomeAppliancesDetails(request, homeAppliances_id):
    if request.method == "GET":
        homeAppliances= HomeAppliances.objects.filter(id = homeAppliances_id)
        serializer = HomeAppliancesSerializer(homeAppliances, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getHomeAppliancesByHomeAppliancesCategory(request, homeAppliancescategory_id):
    if request.method == "GET":
        homeAppliancescategory = get_object_or_404(HomeAppliancesCategory, id=homeAppliancescategory_id)
        homeAppliances = HomeAppliances.objects.filter(category=homeAppliancescategory)
        serializer = HomeAppliancesSerializer(homeAppliances, many=True)
        return Response(serializer.data)