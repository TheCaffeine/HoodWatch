from django.db import migrations, models
 import django.db.models.deletion


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0006_auto_20191027_1826'),
     ]

     operations = [
         migrations.CreateModel(
             name='Post',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('post', models.TextField()),
                 ('date', models.DateTimeField(auto_now_add=True)),
                 ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hood.NeighbourHood')),
                 ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='hood.Profile')),
             ],
         ),
     ]
