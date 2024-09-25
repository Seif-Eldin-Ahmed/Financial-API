from rest_framework import generics
from safe.models import transaction
from .serializers import transactionSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum


# Create your views here :

# This for default page to see the transactions that were made and to create new ones.
class transactionListCreate(generics.ListCreateAPIView):
    queryset = transaction.TransactionObjects.all()
    serializer_class = transactionSerializer

# a Page for returns all transactions that were made.
class transactionList(generics.ListAPIView):
    queryset = transaction.TransactionObjects.all()
    serializer_class = transactionSerializer

# a Page for returns all transactions that were made by using the ID of each transaction.
class transactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = transaction.TransactionObjects.all()
    serializer_class = transactionSerializer

# a Page for creating a new transaction.
class transactionCreate(generics.CreateAPIView):
    queryset = transaction.TransactionObjects.all()
    serializer_class = transactionSerializer

# a Page for updating on any transaction we made by their ID.
class transactionUpdate(generics.UpdateAPIView):
    queryset = transaction.TransactionObjects.all()
    serializer_class = transactionSerializer

# a Page for deleting any transaction we made by their ID.
class transactionDelete(generics.DestroyAPIView):
    queryset = transaction.TransactionObjects.all()
    serializer_class = transactionSerializer    

# a Page for returns all the registered users.
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# a Page allows users to retrieve their transactions based on user ID. 
class UserIdTransactionListView(generics.ListAPIView):
    serializer_class = transactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        try:
            return transaction.TransactionObjects.filter(user_id=user_id)
        
        except User.DoesNotExist:
            return transaction.TransactionObjects.none()

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        return super().get(request, *args, **kwargs)


# a Page to generate financial reports for all given users.
class AllUsersFinancialReportView(APIView):

    def get(self, request):
        users = User.objects.all()
        # Check if the user does not exist
        if not users.exists():
            return Response({"message": "No users found."}, status=status.HTTP_404_NOT_FOUND)

        reports = []
        # To repeat on each of the registered users
        for user in users:
            # Get the user's transactions
            transactions = transaction.objects.filter(user_id=user)
            serialized_transactions = transactionSerializer(transactions, many=True).data
            total_transactions = len(transactions)
            total_amount = sum(transaction.amount for transaction in transactions)

            user_transactions = {
                'user': {
                    'user_id': user.id,
                    'username': user.username,
                    'firstname': user.first_name,
                    'lastname':user.last_name,
                    'email': user.email,
                },
                'transactions': serialized_transactions,
                'total_transactions': total_transactions,
                'total_amount': total_amount

            }
            reports.append(user_transactions)

        return Response(reports)


# a Page to generate financial reports for each user by their ID
class UserFinancialReportView(APIView):

    def get(self, request, user_id):
        # Check if the user exists
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the user's transactions
        transactions = transaction.objects.filter(user_id=user_id)
        if not transactions.exists():
            return Response({"message": "No transactions found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serialized_transactions = transactionSerializer(transactions, many=True).data
        total_transactions = len(transactions)
        total_amount = sum(transaction.amount for transaction in transactions)

        report = {
            'user': {
                'user_id': user.id,
                'username': user.username,
                'firstname': user.first_name,
                'lastname':user.last_name,
                'email': user.email,
            },
            'transactions': serialized_transactions,
            'total_transactions': total_transactions,
            'total_amount': total_amount,
            
        }
        return Response(report)






































# class ReportView(generics.GenericAPIView):
#     permission_classes = [IsAdminUser]  # Only admin users can access this view

#     def get(self, request):
#         # Aggregate transactions for all users
#         report = []
        
#         queryset = User.objects.all()
#         for user_id in queryset:
#             Transactions = transaction.TransactionObjects.filter(user_id=user_id)


#             user_report = {
#                 "user_id": User.id,
#                 "username": User.username,
#                 "title": transaction.title,
#                 # "amount": str(transaction.amount),
#                 # "transaction_date": str(transaction.transaction_date),
#                 # "transaction_count": Transactions.count(),
#             }
#             report.append(user_report)

#         return Response(report)




# class UserTransactionReport(generics.ListAPIView):
#     serializer_class = transactionSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user_id = self.request.query_params.getlist('user_id')
#         if user_id:
#             return transaction.objects.filter(user_id__in=user_id)
#         return transaction.objects.none()  # Return an empty queryset if no user IDs are provided

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)



# class FinancialReportView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user_id = request.user
#         transactions = transaction.objects.filter(user_id=user_id)

#         if not transactions.exists():
#             return Response({"message": "No transactions found for this user."}, status=status.HTTP_404_NOT_FOUND)

#         total_amount = sum(transaction.amount for transaction in transactions)
        
#         serializer_class = transactionSerializer(transactions, many=True).data
        
#         report = {
#             'user': user_id.username,
#             'total_transactions': len(transactions),
#             'total_amount': total_amount,
#             'transactions': serializer_class
#         }

#         return Response(report)
    

    