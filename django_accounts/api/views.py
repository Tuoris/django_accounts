from rest_framework import viewsets

from api.models import Account
from api.serializers import AccountSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
