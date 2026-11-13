from django.db import models


class TimeSlot(models.Model):
    class Day(models.TextChoices):
        MONDAY = "Monday", "Monday"
        TUESDAY = "Tuesday", "Tuesday"
        WEDNESDAY = "Wednesday", "Wednesday"
        THURSDAY = "Thursday", "Thursday"
        FRIDAY = "Friday", "Friday"

    day = models.CharField(max_length=9, choices=Day.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)

    class Meta:
        ordering = [
            models.Case(
                models.When(day="Monday", then=1),
                models.When(day="Tuesday", then=2),
                models.When(day="Wednesday", then=3),
                models.When(day="Thursday", then=4),
                models.When(day="Friday", then=5),
                output_field=models.IntegerField(),
            ),
            "start_time",
        ]
        verbose_name = "time slot"
        verbose_name_plural = "time slots"

    def __str__(self):
        return f"{self.day} {self.start_time:%H:%M}-{self.end_time:%H:%M}: {self.subject_name}"
