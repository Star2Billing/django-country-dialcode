from django.db import models
from django.utils.translation import ugettext as _
from datetime import *
from common.intermediate_model_base_class import Model

prefix_type_list = ((0, _("Landline")),
                    (1, _("Mobile")),
                    (2, _("NGN (Non Geographic Numbers)")))


# Create your models here.
class Country(Model):
    """
    Country

    These are the countries and their country code, country prefix, name
    For instance : USA, 1, United States
    """
    countrycode = models.CharField(max_length=240, verbose_name='Code',
                                   help_text=_("Enter Country Code. e.g. USA"))
    countryprefix = models.IntegerField(max_length=12,
                                   verbose_name='Prefix',
                                   help_text=_("Enter Country Prefix. e.g. 1"))
    countryname = models.CharField(max_length=240, verbose_name='Name',
                         help_text=_("Enter Country Name. e.g. United States"))

    class Meta:
        db_table = 'simu_country'
        app_label = _('prefix_country')
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __unicode__(self):
        return "%s" % (self.countrycode)


class Prefix(Model):
    """
    Prefix

    These are the prefixes and destinations
    For instance : 44 ; United Kingdom
    """
    prefix = models.IntegerField(primary_key=True, help_text=_("Enter Prefix"))
    destination = models.CharField(max_length=180,
                                   help_text=_("Enter Destination"))
    country_id = models.ForeignKey(Country, db_column="country_id", null=True,
                                   blank=True, verbose_name="Country Code",
                                   help_text=_("Select Country"))
    carrier_name = models.CharField(max_length=180,
                                    help_text=_("Enter Carrier Name"))
    prefix_type = models.IntegerField(choices=prefix_type_list, default=1,
                                      verbose_name='Prefix Type',
                                      help_text=_("Select Prefix Type"))

    class Meta:
        db_table = 'simu_prefix'
        app_label = _('prefix_country')
        verbose_name = _("Prefix")
        verbose_name_plural = _("Prefixes")
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
    country_name.short_description = _("Country Name")
