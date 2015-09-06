from rest_framework import generics
from rest_framework import status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CreateAccountSerializer
from .serializers import AccountSerializer
from .models import Account


class AccountCreateViewHandler(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer


class AccountListViewHandler(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountDetailViewHandler(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)    


class MeDetailViewHandler(APIView):
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        me = request.user
        serializer = AccountSerializer(me)
        return Response(serializer.data, status=status.HTTP_200_OK)
