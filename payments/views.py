from django.shortcuts import render
import razorpay
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here

@api_view(['POST'])
def create_order(request):

    amount = request.data.get('amount')

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    order = client.order.create({
        "amount": int(amount) * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    return Response(order)

#
# @api_view(['GET'])
# def create_order(request):
#
#     client = razorpay.Client(
#         auth=(
#             settings.RAZORPAY_KEY_ID,
#             settings.RAZORPAY_KEY_SECRET
#         )
#     )
#
#     try:
#         payments = client.payment.all()
#         return Response({"success": True})
#     except Exception as e:
#         return Response({"error": str(e)})