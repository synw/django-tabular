# -*- coding: utf-8 -*-

from django.db import models
from .utils import _write_file
from django.utils.translation import ugettext_lazy as _


class Table(models.Model):
    name = models.CharField(max_length=120, verbose_name=_(u"Name"))
    slug = models.CharField(max_length=120, unique=True,
                            db_index=True, verbose_name=_(u"Slug"))
    html = models.TextField(blank=True, verbose_name=_(u'Html'))
    updated = models.DateTimeField(
        blank=True, null=True, verbose_name=_(u'Last update'))
    modelnames = models.CharField(max_length=200, blank=True,
                                  verbose_name=_(u"Associated models"),
                                  help_text="List of model names: ex: User,Group"
                                  )
    generator = models.CharField(
        max_length=120, blank=True, verbose_name=_(u"Generator"))

    class Meta:
        verbose_name = _(u'Table')
        verbose_name_plural = _(u'Tables')

        def __str__(self):
            return self.name

    def generate(self):
        _write_file(self.slug, self.html)
