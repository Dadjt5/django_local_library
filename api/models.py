from django.db import models
import uuid

class Persona(models.Model):
    """Model representing a Person."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID")
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.nombre

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('persona-detail', args=[str(self.id)])

    class Meta:
        ordering = ['id']