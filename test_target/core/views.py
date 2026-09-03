from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from core.serializers import BankAccountSerializer
from core.models import SuperSecretBankAccount


@api_view()
def show_balance(request, pk):
    if request.method == "POST":
        return Response({"message": "hi"})
    qs = SuperSecretBankAccount.objects.get(pk=pk)
    
    return JsonResponse({"message": BankAccountSerializer(qs).data})