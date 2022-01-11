from django.db import migrations
 import pyuploadcare.dj.models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0009_auto_20191028_0711'),
     ]

     operations = [
         migrations.AlterField(
             model_name='neighbourhood',
             name='hood_logo',
             field=pyuploadcare.dj.models.ImageField(),
         ),
     ]
