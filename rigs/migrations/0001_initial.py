# Generated by Django 3.2.18 on 2023-04-25 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, choices=[('Guitar', 'Guitar'), ('Bass', 'Bass'), ('Keyboard', 'Keyboard'), ('Drums', 'Drums'), ('DJ', 'DJ'), ('Studio', 'Studio'), ('Live Sound', 'Live Sound'), ('Orchestra', 'Orchestra'), ('Band', 'Band')], max_length=255)),
                ('description', models.TextField(blank=True)),
                ('gear_list', models.TextField(blank=True)),
                ('featured_image', models.ImageField(blank=True, default='../gear_addict_rig_placeholder_e0o12b', upload_to='images/')),
                ('image_2', models.ImageField(blank=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, upload_to='images/')),
                ('attributes', models.CharField(blank=True, choices=[('Budget', 'Budget'), ('Versatile', 'Versatile'), ('High-End', 'High-End'), ('Tribute', 'Tribute'), ('Acoustic', 'Acoustic'), ('Electric', 'Electric'), ('Analogue', 'Analogue'), ('Digital', 'Digital'), ('Electro-Acoustic', 'Electro-Acoustic'), ('Pro', 'Pro'), ('Wireless', 'Wireless'), ('Portable', 'Portable')], max_length=255)),
                ('budget', models.CharField(blank=True, choices=[('£', '£'), ('££', '££'), ('£££', '£££'), ('££££', '££££'), ('£££££', '£££££')], max_length=255)),
                ('genre', models.CharField(blank=True, choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Hip Hop', 'Hip Hop'), ('Jazz', 'Jazz'), ('Rhythm and Blues', 'Rhythm and Blues'), ('Electro', 'Electro'), ('Classical', 'Classical'), ('Blues', 'Blues'), ('Country', 'Country'), ('Heavy Metal', 'Heavy Metal'), ('Dance', 'Dance'), ('World', 'World'), ('Soul', 'Soul'), ('Punk', 'Punk'), ('Motown', 'Motown'), ('Funk', 'Funk'), ('Alt', 'Alt'), ('Folk', 'Folk'), ('Musical Theatre', 'Musical Theatre'), ('Reggae', 'Reggae'), ('Ska', 'Ska'), ('Latin', 'Latin'), ('Indie', 'Indie'), ('House', 'House'), ('Disco', 'Disco'), ('Easy Listening', 'Easy Listening'), ('Dubstep', 'Dubstep'), ('Experimental', 'Experimental'), ('Rock and Roll', 'Rock and Roll'), ('Swing', 'Swing'), ('Instrumental', 'Instrumental'), ('Ambient', 'Ambient'), ('Trance', 'Trance'), ('Bluegrass', 'Bluegrass'), ('Hardcore', 'Hardcore'), ('Grunge', 'Grunge'), ('Prog', 'Prog')], max_length=255)),
                ('featured', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]