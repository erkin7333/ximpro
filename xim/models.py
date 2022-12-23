from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=300, verbose_name=_("Title")),
        description=models.TextField(verbose_name=_("Description"))
    )
    image = models.ImageField(upload_to='blog')

    def __str__(self):
        return f"{self.safe_translation_getter('title')}"
    class Meta:
        verbose_name = "Blog"




class Location(models.Model):
    loc = models.CharField(max_length=100, verbose_name=_("Location"))
    def __str__(self):
        return self.loc
    class Meta:
        verbose_name = "Location"
