from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0010_auto_20191029_0747'),
     ]

     operations = [
         migrations.AlterField(
             model_name='neighbourhood',
             name='hood_logo',
             field=models.ImageField(upload_to='images/'),
         ),
     ]
