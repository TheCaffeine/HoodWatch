from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0001_initial'),
     ]

     operations = [
         migrations.RemoveField(
             model_name='profile',
             name='profile_image',
         ),
         migrations.AddField(
             model_name='profile',
             name='profile_picture',
             field=models.ImageField(default='default.png', upload_to='images/'),
         ),
     ]