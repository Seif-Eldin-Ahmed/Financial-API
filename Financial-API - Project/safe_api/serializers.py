from rest_framework import serializers
from safe.models import transaction
from django.contrib.auth.models import User

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = ('id', 'title','description', 'amount','user_id', 'status', 'transaction_date')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'id']