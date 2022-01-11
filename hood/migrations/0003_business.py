from django.db import migrations, models
 import django.db.models.deletion


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0002_auto_20191026_1329'),
     ]

     operations = [
         migrations.CreateModel(
             name='Business',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('name', models.CharField(max_length=120)),
                 ('email', models.EmailField(max_length=254)),
                 ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hood.NeighbourHood')),
                 ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='hood.Profile')),
             ],
         ),
     ]