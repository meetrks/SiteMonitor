import tldextract

from base.serializers import BaseModelSerializer
from monitor.models import SiteDetail


class SiteDetailSerializer(BaseModelSerializer):
    class Meta:
        model = SiteDetail
        fields = '__all__'

    def validate_site_url(self, attrs):
        protocol = 'https' if attrs.startswith('https') else "http"
        protocol += "://"
        ext = tldextract.extract(attrs)
        print (ext.subdomain, ext.domain, ext.suffix)
        domain = "{subdomain}.{domain}".format(subdomain=ext.subdomain,
                                               domain=ext.domain) if ext.subdomain else ext.domain
        main_url = "{protocol}{domain}.{suffix}/".format(protocol=protocol, domain=domain, suffix=ext.suffix)
        return main_url
