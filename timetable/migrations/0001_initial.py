from django.db import migrations, models


def add_sample_time_slots(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    sample_data = [
        ("Monday", "09:00", "10:00", "Mathematics", "Meenakshi", "Room 101"),
        ("Monday", "10:15", "11:15", "Physics", "Arunkumar", "Room 102"),
        ("Tuesday", "09:00", "10:00", "English", "Kavya", "Room 103"),
        ("Tuesday", "10:15", "11:15", "Chemistry", "Karthik", "Lab 1"),
        ("Wednesday", "09:00", "10:00", "Computer Science", "Yazhini", "Lab 2"),
        ("Wednesday", "10:15", "11:15", "Mathematics", "Meenakshi", "Room 101"),
        ("Thursday", "09:00", "10:00", "Biology", "Tamilchelvi", "Lab 3"),
        ("Thursday", "10:15", "11:15", "History", "Ilango", "Room 104"),
        ("Friday", "09:00", "10:00", "Physics", "Arunkumar", "Room 102"),
        ("Friday", "10:15", "11:15", "Computer Science", "Yazhini", "Lab 2"),
    ]
    TimeSlot.objects.using(schema_editor.connection.alias).bulk_create(
        [
            TimeSlot(
                day=day,
                start_time=start_time,
                end_time=end_time,
                subject_name=subject,
                faculty_name=faculty,
                classroom=classroom,
            )
            for day, start_time, end_time, subject, faculty, classroom in sample_data
        ]
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TimeSlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                        ],
                        max_length=9,
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("subject_name", models.CharField(max_length=100)),
                ("faculty_name", models.CharField(max_length=100)),
                ("classroom", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "time slot",
                "verbose_name_plural": "time slots",
                "ordering": ["day", "start_time"],
            },
        ),
        migrations.RunPython(add_sample_time_slots, migrations.RunPython.noop),
    ]
