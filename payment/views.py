from django.shortcuts import render

import requests
import json

# Fonction pour effectuer un paiement avec MTN MoMo
def make_mtn_momo_payment(amount, phone_number):
    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"
    headers = {
        "X-Reference-Id": "123456",
        "Ocp-Apim-Subscription-Key": "YOUR_SUBSCRIPTION_KEY",
        "X-Target-Environment": "sandbox",
        "Content-Type": "application/json"
    }
    data = {
        "amount": amount,
        "currency": "EUR",
        "externalId": "123456",
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": phone_number
        },
        "payerMessage": "Payment for services",
        "payeeNote": "Thank you for your payment"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Exemple d'utilisation de la fonction
payment_response = make_mtn_momo_payment(1000, "256771234567")
print(payment_response)

