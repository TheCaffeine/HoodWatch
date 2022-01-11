from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0005_auto_20191027_1825'),
     ]

     operations = [
         migrations.AlterField(
             model_name='neighbourhood',
             name='health',
             field=models.IntegerField(blank=True, null=True),
         ),
         migrations.AlterField(
             model_name='neighbourhood',
             name='police',
             field=models.IntegerField(blank=True, null=True),
         ),
     ]
