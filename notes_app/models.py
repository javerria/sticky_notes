from django.db import models


class StickyNote(models.Model):
    """
    A model representing a sticky note.

    Attributes:
        title (CharField): The title of the sticky note
        content (CharField): The main content of the sticky note
        created_on (DateTimeField): The date and time when the note was created, 
            which is automatically set to the current date and time when the note is created.
        author (CharField): The author of the sticky note. This field is optional.
    """

    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the sticky note.

        Returns:
            str: The title of the sticky note.
        """
        return self.title
