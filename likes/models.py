from django.db import models
from django.contrib.auth.models import User
from rigs.models import Rig


class Like(models.Model):
    """
    Like model, related to 'owner' and 'rig'
    'owner' is a User instance and 'rig' is a Rig instance
    'unique_together' makes sure a user can't like the same rig twice
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rig = models.ForeignKey(
        Rig,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'rig']

    def __str__(self):
        return f'{self.owner} {self.rig}'
