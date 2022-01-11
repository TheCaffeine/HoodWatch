from django.db import migrations, models
 import django.db.models.deletion


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0003_auto_20191026_1129'),
     ]

     operations = [
         migrations.AlterField(
             model_name='profile',
             name='neighbourhood',
             field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='hood.NeighbourHood'),
         ),
     ]