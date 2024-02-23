from django.db import models

class ParkingSlot(models.Model):
    slot_number = models.IntegerField()
    availability = models.CharField(max_length=20)

    def __str__(self):
        return f"Slot {self.slot_number}: {self.availability}"
