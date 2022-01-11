from django.db import migrations


 class Migration(migrations.Migration):

     dependencies = [
         ('hood', '0015_auto_20191029_0910'),
     ]

     operations = [
         migrations.RenameField(
             model_name='neighbourhood',
             old_name='health',
             new_name='health_tell',
         ),
         migrations.RenameField(
             model_name='neighbourhood',
             old_name='police',
             new_name='police_number',
         ),
     ]
