from django.test import TestCase

from .models import TimeSlot


class TimetableViewTests(TestCase):
    def test_displays_seeded_records_in_weekday_order(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Class Timetable")
        self.assertEqual(response.context["time_slots"].count(), 10)
        self.assertEqual(
            list(
                dict.fromkeys(
                    response.context["time_slots"].values_list("day", flat=True)
                )
            ),
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        )
        self.assertContains(response, "Room 101")
        self.assertContains(response, "Meenakshi")

    def test_displays_message_when_timetable_is_empty(self):
        TimeSlot.objects.all().delete()

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No timetable records are available.")
