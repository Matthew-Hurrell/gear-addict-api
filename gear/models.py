from django.db import models
from django.contrib.auth.models import User


class Gear(models.Model): 
    """
    Gear model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    # Category Choices
    category_choices = (
        ('Guitar', 'Guitar'),
        ('Bass', 'Bass'),
        ('Keyboard', 'Keyboard'),
        ('Amplifier', 'Amplifier'),
        ('Drums', 'Drums'),
        ('DJ', 'DJ'),
        ('Studio', 'Studio'),
        ('Live Sound', 'Live Sound'),
        ('Orchestra', 'Orchestra'),
        ('Band', 'Band'),
        ('Lights', 'Lights'),
        ('Accessories', 'Accessories')
    )

    # Condition Choices
    condition_choices = (
        ('Non-Functioning', 'Non-Functioning'),
        ('Poor', 'Poor'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
        ('Excellent', 'Excellent'),
        ('Mint', 'Mint')
    )

    # Repair Choices
    repair_choices = (
        (0, "No"),
        (1, "Yes")
    )

    # Sale Choices
    sale_choices = (
        (0, "No"),
        (1, "Yes")
    )

    # Insured Choices
    insured_choices = (
        (0, "No"),
        (1, "Yes")
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=255,
        choices=category_choices,
        blank=True
    )
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    serial = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=100, blank=True)
    condition = models.CharField(
        max_length=100,
        choices=condition_choices,
        blank=True
    )
    value = models.PositiveIntegerField()
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../gear-placeholder_l5xkcjb',
        blank=True
    )
    repair = models.IntegerField(choices=repair_choices, default=0)
    sale = models.IntegerField(choices=sale_choices, default=0)
    insured = models.IntegerField(choices=insured_choices, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'
