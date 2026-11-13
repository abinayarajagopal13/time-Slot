from django.db import migrations


NAME_TRANSLATIONS = {
    "டாக்டர் மீனாட்சி": "மீனாட்சி",
    "பேராசிரியர் அருண்குமார்": "அருண்குமார்",
    "செல்வி காவ்யா": "காவ்யா",
    "டாக்டர் கார்த்திக்": "கார்த்திக்",
    "செல்வி யாழினி": "யாழினி",
    "டாக்டர் தமிழ்ச்செல்வி": "தமிழ்ச்செல்வி",
    "திரு இளங்கோ": "இளங்கோ",
}


def remove_titles_and_surnames(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    database = schema_editor.connection.alias
    for old_name, short_name in NAME_TRANSLATIONS.items():
        TimeSlot.objects.using(database).filter(faculty_name=old_name).update(
            faculty_name=short_name
        )


def restore_full_names(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    database = schema_editor.connection.alias
    for old_name, short_name in NAME_TRANSLATIONS.items():
        TimeSlot.objects.using(database).filter(faculty_name=short_name).update(
            faculty_name=old_name
        )


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0003_translate_sample_faculty_names"),
    ]

    operations = [
        migrations.RunPython(remove_titles_and_surnames, restore_full_names),
    ]
