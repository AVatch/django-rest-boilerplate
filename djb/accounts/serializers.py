import datetime

from rest_framework import serializers

from .models import Account


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        account = Account(
          email=validated_data.get('email'),
          first_name=validated_data.get('first_name', ''),
          last_name=validated_data.get('last_name', '')
        )
        account.set_password(validated_data['password'])
        account.save()
        return account


class AccountSerializer(serializers.ModelSerializer):
    # we make email read only since it is the unique identifier
    # for the account. To update email and password implement
    # a proper update flow
    email = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    # Demonstrate a dynamic call in the serializer
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('id', 'email', 'first_name', 'last_name',
                  'time_created', 'time_updated', 'is_admin',
                  'full_name')

    def get_full_name(self, obj):
        # Dynamic call gets executed here
        return obj.get_full_name()