from django.shortcuts import render

from .models import TimeSlot


def timetable(request):
    time_slots = TimeSlot.objects.all()
    return render(request, "timetable/timetable.html", {"time_slots": time_slots})
