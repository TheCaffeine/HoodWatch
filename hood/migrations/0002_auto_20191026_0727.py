from django.conf import settings
 from django.db import migrations, models
 import django.db.models.deletion


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0001_initial'),
     ]

     operations = [
         migrations.RemoveField(
             model_name='profile',
             name='profile_image',
         ),
         migrations.AddField(
             model_name='profile',
             name='profile_picture',
             field=models.ImageField(default='default.png', upload_to='images/'),
         ),
         migrations.AlterField(
             model_name='profile',
             name='user',
             field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
         ),
         migrations.CreateModel(
             name='NeighbourHood',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('name', models.CharField(max_length=50)),
                 ('location', models.CharField(max_length=60)),
                 ('logo', models.ImageField(default='hoodlogo.png', upload_to='images/')),
                 ('description', models.TextField()),
                 ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='hood.Profile')),
             ],
         ),
         migrations.AddField(
             model_name='profile',
             name='neighbourhood',
             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='hood.NeighbourHood'),
         ),
     ]