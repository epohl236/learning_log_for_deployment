from django.db import models
from django.contrib.auth.models import User


class Topic (models.Model):
    """A topic the user is learning about."""

    text = models.CharField (max_length=200)
    date_added = models.DateTimeField (auto_now_add=True)
    # Make the topic be owned by a certain user.
    # If the user is deleted, all of his topics are deleted.
    owner = models.ForeignKey (User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    

class Entry (models.Model):
    """Something specific learned about a topic"""

    topic = models.ForeignKey (Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField (auto_now_add=True)

    class Meta:
        """Provides the plural of 'entry' to Django. Otherwise it would
        use 'entrys'."""
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry"""
        CLIPLENGTH = 50

        return self.text if len (self.text) <= CLIPLENGTH \
                else self.text[:CLIPLENGTH] + "..."

    