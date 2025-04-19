from django.db import models

class Code(models.Model):
    content = models.TextField()
    origin = models.CharField(max_length=10, choices=[('com IA', 'Com IA'), ('sem IA', 'Sem IA')])
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin} - {self.send_date}"