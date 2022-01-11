from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0007_post'),
     ]

     operations = [
         migrations.AddField(
             model_name='profile',
             name='location',
             field=models.CharField(blank=True, max_length=50),
         ),
     ]
