import urllib3
from django.utils.crypto import get_random_string

ALLOWED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

urllib3.disable_warnings()
http = urllib3.PoolManager()

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def generate_short_id(id_length=8):
    return get_random_string(length=id_length, allowed_chars=ALLOWED_CHARS)


def get_site_status(site_url):
    try:
        if site_url:
            r = http.request('GET', site_url, headers=header)
            return r.status
    except:
        pass
    return None
