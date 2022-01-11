 from django.conf import settings
 from django.db import migrations, models
 import django.db.models.deletion
 import pyuploadcare.dj.models


 class Migration(migrations.Migration):

     initial = True

     dependencies = [
         migrations.swappable_dependency(settings.AUTH_USER_MODEL),
     ]

     operations = [
         migrations.CreateModel(
             name='Profile',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('profile_image', pyuploadcare.dj.models.ImageField()),
                 ('name', models.CharField(blank=True, max_length=80)),
                 ('bio', models.TextField(blank=True, max_length=254)),
                 ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
             ],
         ),
     ]
