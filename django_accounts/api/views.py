from rest_framework import viewsets

from api.models import Account
from api.serializers import AccountSerializer, JSONCreateAccountSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_serializer_class(self):
        if self.action == 'create' and self.request.content_type == 'application/json':
            return JSONCreateAccountSerializer
        return AccountSerializer
