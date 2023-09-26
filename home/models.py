from django.db import models

# Create your models here.


# تعریف گزینه‌های ممکن برای type_of_service
SERVICE_CHOICES = (
    (1, 'خدمت نصب'),
    (2, 'خدمت تعمیر'),
    (3, 'خدمت دیگر'),
)


class CustomerRequest(models.Model):
    #customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    type_of_service = models.IntegerField()
    device_name = models.CharField(max_length=100)
    request_date=models.DateTimeField()
    is_done = models.BooleanField()

    # class Meta:
    #     db_table = 'customer_service'
