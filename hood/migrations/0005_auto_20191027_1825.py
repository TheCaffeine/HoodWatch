from django.db import migrations, models


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0004_business_description'),
     ]

     operations = [
         migrations.AddField(
             model_name='neighbourhood',
             name='health',
             field=models.IntegerField(blank=True, max_length=50, null=True),
         ),
         migrations.AddField(
             model_name='neighbourhood',
             name='police',
             field=models.IntegerField(blank=True, max_length=20, null=True),
         ),
     ]
