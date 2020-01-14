# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from country_dialcode.intermediate_model_base_class import Model

prefix_type_list = ((0, "Landline"),
                    (1, "Mobile"),
                    (2, "NGN (Non Geographic Numbers)"))


# Create your models here.
class Country(Model):
    """
    Country

    These are the countries and their country code, country prefix, name
    For instance : USA, 1, United States
    """
    countrycode = models.CharField(max_length=3, verbose_name=_('ISO alpha-3'),
                                   help_text=_("Enter Country Code. e.g. USA - ISO alpha-3"))
    iso2 = models.CharField(verbose_name=_('ISO alpha-2'),
                            max_length=2, default='')
    countryprefix = models.IntegerField(verbose_name=_('Prefix'),
                                        help_text=_("Enter Country Prefix. e.g. 1"))
    countryname = models.CharField(max_length=240, verbose_name=_('Name'),
                                   help_text=_("Enter Country Name. e.g. United States"))

    class Meta:
        db_table = 'dialcode_country'
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __unicode__(self):
        return "%s" % (self.countrycode)


class Prefix(Model):
    """
    Prefix

    These are the prefixes and destinations
    For instance : 44 ; United Kingdom
    """
    prefix = models.IntegerField(primary_key=True, help_text=_("enter prefix"))
    destination = models.CharField(max_length=180, help_text=_("enter destination"))
    country_id = models.ForeignKey(Country,
                                   db_column="country_id", null=True,
                                   blank=True, verbose_name=_("country code"),
                                   help_text=_("select country"), on_delete=models.CASCADE)
    carrier_name = models.CharField(max_length=180, help_text=_("enter carrier name"))
    prefix_type = models.IntegerField(choices=prefix_type_list, default=1,
                                      verbose_name=_('prefix type'),
                                      help_text=_("select prefix type"))

    class Meta:
        db_table = 'dialcode_prefix'
        verbose_name = _("prefix")
        verbose_name_plural = _("prefixes")
        ordering = ["prefix"]

    def __unicode__(self):
        return "%d" % (self.prefix)

    def country_name(self):
        """
        Return country name on country listing (changeview_list)
        """
        if self.country_id is None:
            return ""
        else:
            return self.country_id.countryname
    country_name.short_description = _("country name")
