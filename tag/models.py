from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # For generic relation, we need 2 things
    # (1) - Type of the object
    # (2) - id of the object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()