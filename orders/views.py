from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import Status
from django.utils import timezone

# Create your views here.
class CouponValidationView(APIView):
    """
    Validates coupon code sent from client
    """
    def post(self,request,*args,**kwargs):
        code = request.data.get("code")
        if not code:
            return Response({"error":"Coupon code is required"}, status=status.HTTP_400_BAD_Request)
        
        today = timezone.now().date()
        try:
            coupon = Coupon.objects.get(coupon_code=coupon)
        except Coupon.DoesNotExist:
            return Response({"error":"Invalid code"},status=status.HTTP_400_BAD_Request)
        
        if not coupon.is_active:
            return Response({"error":"Coupon inactive"},status=status.HTTP_400_BAD_Request)
        
        if not (coupon.valid_from <= today <= valid_until):
            return Response({"error":"Coupon not valid at this time"},status=status.HTTP_400_BAD_Request)

        return Response({
            "success":True,
            "discount":float(coupon.discount_percentage),
        },
        status=status.HTTP_200_OK
        )