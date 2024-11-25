from django.shortcuts import render
from django.http import HttpResponse
import requests

from . mpesa import AccessToken, Password


# Create your views here.
def home(request):
    return render(request,'home.html')

def pay(request):
    return render(request,'pay.html')

def stk(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST['amount']
        access_token = AccessToken.access_token
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        header = {"Authorization": "Bearer %s" % access_token}

        request = {
            "BusinessShortCode": Password.shortcode,
            "Password": Password.decoded_password,
            "Timestamp": Password.timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": Password.shortcode,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",
            "AccountReference": "Mercy",
            "TransactionDesc": "Fee payment"
        }

    response = requests.post(api_url, json=request, headers=header)
    return HttpResponse('success')