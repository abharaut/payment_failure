import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Payments
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    payments = Payments.objects.all()
    return render(request, "index.html", {"payments": list(payments)})

        
@csrf_exempt
def webhook(request):
    payload = json.loads(request.body)["data"]["object"]
    payment = Payments(transaction_id=payload["id"], amount=payload["amount"], status=payload["status"], failure_reason=payload.get("failure_message", "-"))
    payment.save()
    return JsonResponse({"messsage": "success"})