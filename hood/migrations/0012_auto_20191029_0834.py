from django.db import migrations
 import pyuploadcare.dj.models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0011_auto_20191029_0832'),
     ]

     operations = [
         migrations.AlterField(
             model_name='neighbourhood',
             name='hood_logo',
             field=pyuploadcare.dj.models.ImageField(),
         ),
     ]
