from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0016_auto_20191029_0911'),
     ]

     operations = [
         migrations.AddField(
             model_name='post',
             name='title',
             field=models.CharField(max_length=120, null=True),
         ),
     ]
