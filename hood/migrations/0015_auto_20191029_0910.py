from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0014_auto_20191029_0852'),
     ]

     operations = [
         migrations.RemoveField(
             model_name='neighbourhood',
             name='health_tell',
         ),
         migrations.RemoveField(
             model_name='neighbourhood',
             name='police_number',
         ),
         migrations.AddField(
             model_name='neighbourhood',
             name='health',
             field=models.IntegerField(blank=True, null=True),
         ),
         migrations.AddField(
             model_name='neighbourhood',
             name='police',
             field=models.IntegerField(blank=True, null=True),
         ),
     ]
