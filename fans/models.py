from django.db import models
from django.contrib.auth.models import User


class Fan(models.Model):
    """
    Fan model, related to 'fan' and 'idol'
    We need the related_name attribute so that django can differentiate
    between 'fan' and 'idol' who both are User model instances
    'unique_together' makes sure a user can't double fan the same user
    """
    fan = models.ForeignKey(
        User,
        related_name='fanboy',
        on_delete=models.CASCADE
    )
    idol = models.ForeignKey(
        User,
        related_name='idolguy',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['fan', 'idol']

    def __str__(self):
        return f'{self.fan} {self.idol}'
