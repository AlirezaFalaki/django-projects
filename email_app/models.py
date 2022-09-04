from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Email(models.Model):
    author = models.ForeignKey(User, related_name='emails', on_delete=models.CASCADE)
    recipients = models.ManyToManyField(User, related_name='ReceiveEmails')
    title = models.CharField(max_length=100)
    body = models.TextField()
    attacht = models.FileField(verbose_name="attachment", upload_to='email-files')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + '--' + self.title
