from django.db import migrations


NAME_TRANSLATIONS = {
    "Dr. Ananya Rao": "டாக்டர் மீனாட்சி",
    "Prof. Vikram Shah": "பேராசிரியர் அருண்குமார்",
    "Ms. Priya Nair": "செல்வி காவ்யா",
    "Dr. Rahul Menon": "டாக்டர் கார்த்திக்",
    "Ms. Kavya Iyer": "செல்வி யாழினி",
    "Dr. Meera Das": "டாக்டர் தமிழ்ச்செல்வி",
    "Mr. Arjun Bose": "திரு இளங்கோ",
}


def translate_faculty_names(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    database = schema_editor.connection.alias
    for old_name, tamil_name in NAME_TRANSLATIONS.items():
        TimeSlot.objects.using(database).filter(faculty_name=old_name).update(
            faculty_name=tamil_name
        )


def restore_faculty_names(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    database = schema_editor.connection.alias
    for old_name, tamil_name in NAME_TRANSLATIONS.items():
        TimeSlot.objects.using(database).filter(faculty_name=tamil_name).update(
            faculty_name=old_name
        )


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0002_alter_timeslot_options"),
    ]

    operations = [
        migrations.RunPython(translate_faculty_names, restore_faculty_names),
    ]
