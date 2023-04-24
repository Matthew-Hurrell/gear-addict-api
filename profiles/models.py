from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    # Instruments Choices
    instruments_choices = (
        ('Electic Guitar', 'Electic Guitar'),
        ('Acoustic Guitar', 'Acoustic Guitar'),
        ('Bass Guitar', 'Bass Guitar'),
        ('Drums', 'Drums'),
        ('Percussion', 'Percussion'),
        ('Piano', 'Piano'),
        ('Keyboard', 'Keyboard'),
        ('Vocals', 'Vocals'),
        ('Saxophone', 'Saxophone'),
        ('Ukulele', 'Ukulele'),
        ('Violin', 'Violin'),
        ('Cello', 'Cello'),
        ('Trumpet', 'Trumpet'),
        ('Clarinet','Clarinet'),
        ('Accordion', 'Accordion'),
        ('Xylophone', 'Xylophone'),
        ('Trombone', 'Trombone'),
        ('Flute', 'Flute'),
        ('Oboe', 'Oboe'),
        ('Harp', 'Harp'),
        ('Harmonica', 'Harmonica'),
        ('Mandolin', 'Mandolin'),
        ('Bassoon', 'Bassoon'),
        ('Tuba', 'Tuba'),
        ('Viola', 'Viola'),
        ('Double Bass', 'Double Bass'),
        ('Synthesiser', 'Synthesiser'),
        ('Banjo', 'Banjo'),
        ('Bagpipes', 'Bagpipes'),
        ('Classical Guitar', 'Classical Guitar'),
        ('Cajon', 'Cajon'),
        ('Organ', 'Organ'),
        ('Didgeridoo', 'Didgeridoo'),
        ('Sitar', 'Sitar')
    )

    # Genres Choices
    genres_choices = (
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

    # Expertise Choices
    expertise_choices = (
        ('Beginner', 'Beginner'),
        ('Novice', 'Novice'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
        ('Pro', 'Pro')
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../rock-hand-gesture_eajhnb', blank=True
    )
    header_image = models.ImageField(
        upload_to='images/', default='../default_header_jtvt3u', blank=True
    )
    location = models.CharField(max_length=255, blank=True)
    instruments = models.CharField(
        max_length=255, choices=instruments_choices, blank=True
    )
    genres = models.CharField(
        max_length=255, choices=genres_choices, blank=True
    )
    expertise = models.CharField(
        max_length=255, choices=expertise_choices, blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)    

# post_save.connect(create_profile, sender=User)

