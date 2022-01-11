 from django.conf import settings
 from django.db import migrations, models
 import django.db.models.deletion


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0002_auto_20191026_0727'),
     ]

     operations = [
         migrations.AlterField(
             model_name='profile',
             name='user',
             field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
         ),
     ]