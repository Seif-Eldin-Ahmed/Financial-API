from django.urls import path
from .views import *

app_name = 'safe_api'

urlpatterns = [
    # Our endpoints for this API project
    path('', transactionListCreate.as_view(), name='transaction-List-creation'),
    path('transactions/', transactionList.as_view(), name='transactions-list'),
    path('transactions/<int:pk>/', transactionDetail.as_view(), name='transactions-details-by_id'),

    path('transactions/create/', transactionCreate.as_view(), name='transactions-creation'),
    path('transactions/update/<int:pk>/', transactionUpdate.as_view(), name='transactions-update-by_id'),
    path('transactions/delete/<int:pk>/', transactionDelete.as_view(), name='transactions-delete-by_id'),

    path('users/', UserListView.as_view(), name='users-list'),
    path('users/<int:user_id>/transactions/', UserIdTransactionListView.as_view(), name='user-transaction'),

    path('reports/', AllUsersFinancialReportView.as_view(), name='all-users-financial-report'),    
    path('reports/<int:user_id>/', UserFinancialReportView.as_view(), name='user-financial-report'),   

]   






# path('reports/', ReportView.as_view(), name='financial-reports'),

    # path('reports/', UserTransactionReport.as_view(), name='user-transaction-report'),

    # path('reports/', FinancialReportView.as_view(), name='financial-report'),