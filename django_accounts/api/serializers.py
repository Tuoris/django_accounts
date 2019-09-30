from rest_framework import serializers

from api.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'avatar',
            'first_name',
            'last_name',
            'creation_date',
        ]
