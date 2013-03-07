from django import template
from django.template.defaultfilters import stringfilter
from country_dialcode.models import Country
from country_dialcode.utils.isoflag import iso_flag as util_iso_flag
from django.utils.translation import gettext as _
register = template.Library()


@stringfilter
def iso_flag(country_id, flag_path=u''):
    """
    Returns a full path to the ISO 3166-1 alpha-2 country code flag image.

    Example usage::

        {{ user_profile.country_dialcode.country_id|iso_flag }}

        {{ user_profile.country_dialcode.country_id|iso_flag:"appmedia/flags/%s.png" }}

    """
    if country_id == '999':
        #Added for internal call - ie flag/phone.png
        return util_iso_flag('telephone', flag_path)
    try:
        obj_country = Country.objects.get(id=country_id)
    except:
        return u''
    return util_iso_flag(obj_country.iso2, flag_path)

register.filter('iso_flag', iso_flag)


@stringfilter
def country_name(country_id):
    """
    Returns a country name

    >>> country_name(198)
    u'Spain'
    """
    if country_id == '999':
        #Added for internal call - ie flag/phone.png
        return _('internal call').title()
    try:
        obj_country = Country.objects.get(id=country_id)
        return obj_country.countryname
    except:
        return _('unknown')

register.filter('country_name', country_name)
