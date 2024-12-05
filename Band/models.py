from django.db import models


# Create your models here.
class Event(models.Model):
    """
    Model representing an event for the band, including event name,
    date, location, and description.
    Attributes:
        name (str): The name of the event.
        date(date): The date of the event.
        location (str): The location where the event will take place.
        description (str): A description providing more details
        about the event.
    """
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the event in the format:
        "Event Name - Event Date."

        Returns:
            str: A string representation of the event.
        """
        return f"{self.name} - {self.date}"
