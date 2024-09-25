from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class transaction(models.Model):

    class transactionObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    options = (
        ('noted', 'Noted'),
        ('reject', 'Reject'),
        ('success', 'Success')
    )

    Category = models.ForeignKey(
        category, on_delete=models.PROTECT, default= 1
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=255)
    transaction_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='transaction_posts'
    )
    status = models.CharField(
        max_length=100, choices=options, default='noted'
    )
    objects = models.Manager()  # default manager
    TransactionObjects = transactionObjects()  # custom manager

    class Meta:
        ordering = ('-transaction_date',)

    def __str__(self):
        return self.title
