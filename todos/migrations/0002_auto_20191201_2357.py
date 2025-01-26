from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(verbose_name='Deadline'),
        ),
    ]
