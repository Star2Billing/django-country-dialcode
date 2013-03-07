from django.contrib import admin
from django.utils.translation import ugettext as _
from country_dialcode.models import Country, Prefix
from common.app_label_renamer import AppLabelRenamer
AppLabelRenamer(native_app_label=u'country_dialcode', app_label=_('Country Dialcode')).main()


class CountryAdmin(admin.ModelAdmin):
    list_display = ('countrycode', 'iso2', 'countryprefix', 'countryname')
    search_fields = ('countryname', 'countryprefix')
    ordering = ('id', )
    list_filter = ['countryprefix', 'countrycode']

    def __init__(self, *args, **kwargs):
        super(CountryAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('countrycode', )
admin.site.register(Country, CountryAdmin)


class PrefixAdmin(admin.ModelAdmin):
    search_fields = ('prefix', 'destination')
    list_display = ('prefix', 'destination', 'country_name', 'carrier_name')
    ordering = ('prefix', )
    #list_filter = ['country_name', 'carrier_name']

    def __init__(self, *args, **kwargs):
        super(PrefixAdmin, self).__init__(*args, **kwargs)
        #self.list_display_links = (None, )
admin.site.register(Prefix, PrefixAdmin)
