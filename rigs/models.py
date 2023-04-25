from django.db import models
from django.contrib.auth.models import User


class Rig(models.Model): 
    """
    Rig model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    # Category Choices
    category_choices = (
        ('Guitar', 'Guitar'),
        ('Bass', 'Bass'),
        ('Keyboard', 'Keyboard'),
        ('Drums', 'Drums'),
        ('DJ', 'DJ'),
        ('Studio', 'Studio'),
        ('Live Sound', 'Live Sound'),
        ('Orchestra', 'Orchestra'),
        ('Band', 'Band')
    )

    # Attributes Choices
    attributes_choices = (
        ('Budget', 'Budget'),
        ('Versatile', 'Versatile'),
        ('High-End', 'High-End'),
        ('Tribute', 'Tribute'),
        ('Acoustic', 'Acoustic'),
        ('Electric', 'Electric'),
        ('Analogue', 'Analogue'),
        ('Digital', 'Digital'),
        ('Electro-Acoustic', 'Electro-Acoustic'),
        ('Pro', 'Pro'),
        ('Wireless', 'Wireless'),
        ('Portable', 'Portable')
    )

    # Budget Choices
    budget_choices = (
        ('£', '£'),
        ('££', '££'),
        ('£££', '£££'),
        ('££££', '££££'),
        ('£££££', '£££££')
    )

    # Genre Choices
    genre_choices = (
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Hip Hop', 'Hip Hop'),
        ('Jazz', 'Jazz'),
        ('Rhythm and Blues', 'Rhythm and Blues'),
        ('Electro', 'Electro'),
        ('Classical', 'Classical'),
        ('Blues', 'Blues'),
        ('Country', 'Country'),
        ('Heavy Metal', 'Heavy Metal'),
        ('Dance', 'Dance'),
        ('World', 'World'),
        ('Soul', 'Soul'),
        ('Punk', 'Punk'),
        ('Motown', 'Motown'),
        ('Funk', 'Funk'),
        ('Alt', 'Alt'),
        ('Folk', 'Folk'),
        ('Musical Theatre', 'Musical Theatre'),
        ('Reggae', 'Reggae'),
        ('Ska', 'Ska'),
        ('Latin', 'Latin'),
        ('Indie', 'Indie'),
        ('House', 'House'),
        ('Disco', 'Disco'),
        ('Easy Listening', 'Easy Listening'),
        ('Dubstep', 'Dubstep'),
        ('Experimental', 'Experimental'),
        ('Rock and Roll', 'Rock and Roll'),
        ('Swing', 'Swing'),
        ('Instrumental', 'Instrumental'),
        ('Ambient', 'Ambient'),
        ('Trance', 'Trance'),
        ('Bluegrass', 'Bluegrass'),
        ('Hardcore', 'Hardcore'),
        ('Grunge', 'Grunge'),
        ('Prog', 'Prog'),
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
    description = models.TextField(blank=True)
    gear_list = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='images/', default='../gear_addict_rig_placeholder_e0o12b',
    blank=True)
    image_2 = models.ImageField(upload_to='images/', blank=True)
    image_3 = models.ImageField(upload_to='images/', blank=True)
    image_4 = models.ImageField(upload_to='images/', blank=True)
    attributes = models.CharField(
        max_length=255,
        choices=attributes_choices,
        blank=True
    )
    budget = models.CharField(
        max_length=255,
        choices=budget_choices,
        blank=True
    )
    genre = models.CharField(
        max_length=255,
        choices=genre_choices,
        blank=True
    )
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f'{self.id} {self.name}'
