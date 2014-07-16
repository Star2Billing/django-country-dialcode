# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Model(models.Model):
    """
    Intermediate model base class.
    """
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.clear_nullable_related()
        super(Model, self).delete(*args, **kwargs)

    def clear_nullable_related(self):
        """
        Recursively clears any nullable foreign key fields on related objects.
        Django is hard-wired for cascading deletes, which is very dangerous for
        us. This simulates ON DELETE SET NULL behavior manually.
        """
        for related in self._meta.get_all_related_objects():
            accessor = related.get_accessor_name()
            try:
                related_set = getattr(self, accessor)
            except ObjectDoesNotExist:
                continue

            if related.field.null:
                related_set.clear()
            elif related.field.rel.multiple:
                for related_object in related_set.all():
                    related_object.clear_nullable_related()
