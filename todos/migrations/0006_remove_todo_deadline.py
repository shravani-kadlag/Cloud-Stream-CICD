from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_auto_20191202_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='deadline',
        ),
    ]
