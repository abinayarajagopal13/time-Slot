from django.db import migrations


NAME_TRANSLATIONS = {
    "மீனாட்சி": "Meenakshi",
    "அருண்குமார்": "Arunkumar",
    "காவ்யா": "Kavya",
    "கார்த்திக்": "Karthik",
    "யாழினி": "Yazhini",
    "தமிழ்ச்செல்வி": "Tamilchelvi",
    "இளங்கோ": "Ilango",
}


def translate_faculty_names(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    database = schema_editor.connection.alias
    for tamil_name, english_name in NAME_TRANSLATIONS.items():
        TimeSlot.objects.using(database).filter(faculty_name=tamil_name).update(
            faculty_name=english_name
        )


def restore_tamil_names(apps, schema_editor):
    TimeSlot = apps.get_model("timetable", "TimeSlot")
    database = schema_editor.connection.alias
    for tamil_name, english_name in NAME_TRANSLATIONS.items():
        TimeSlot.objects.using(database).filter(faculty_name=english_name).update(
            faculty_name=tamil_name
        )


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0004_remove_faculty_titles_and_surnames"),
    ]

    operations = [
        migrations.RunPython(translate_faculty_names, restore_tamil_names),
    ]
