# myapp/models.py
from django.db import models
from django.conf import settings

class RequestModel(models.Model):
    request_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100)
    pnr = models.CharField(max_length=100)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    representative_name = models.CharField(max_length=200)  # Updated field name
    image_data = models.TextField()
    remarks = models.TextField(blank=True, null=True)