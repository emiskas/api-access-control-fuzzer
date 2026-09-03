from rest_framework import serializers
from core.models import SuperSecretBankAccount

class BankAccountSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = SuperSecretBankAccount
        fields = ['owner', 'balance']

