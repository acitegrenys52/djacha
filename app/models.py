from django.db import models


class Chat(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[0:20]
