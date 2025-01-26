from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_remove_todo_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='title',
        ),
    ]
