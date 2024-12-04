from djongo import models
from django.utils.timezone import now

class Payments(models.Model):
    user_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])
    failure_reason = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=now)
    transaction_id = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"
    
    class Meta:
        app_label = "payment"
        db_table = "Payments"

