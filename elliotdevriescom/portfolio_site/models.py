from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    body = models.TextField()
    urgency = models.SmallIntegerField(default=0)
    handled = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)

    def body_preview(self):
        return (self.body[:50] + "[...]") if len(self.body) > 50 else self.body

    def __str__(self):
        return self.subject[:50]
