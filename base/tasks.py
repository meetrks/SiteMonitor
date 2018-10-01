from __future__ import absolute_import

import time

import urllib3
from celery import shared_task

from base.send_sms import send_sms
from members.models import MemberDirectory
from monitor.models import SiteDetail
from roles.models import Role

urllib3.disable_warnings()
http = urllib3.PoolManager()


def alert_user(site):
    site.status = False if site.status else False
    site.last_down_time = int(time.time()) if not site.last_down_time else site.last_down_time
    site.save()
    all_roles = Role.objects.filter(is_active=True)
    now = int(time.time())
    for role in all_roles:
        if now - int(role.last_alert_on) > int(role.alert_diff) * 60:
            role.last_alert_on = now
            role.save()
            users = MemberDirectory.objects.filter(is_active=True)  # , user_role=role)
            send_sms(users=users, site=site)


def get_site_status(site_url):
    try:
        if site_url:
            r = http.request('GET', site_url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            })
            return r.status
    except:
        pass
    return None


@shared_task
def list_n_monitor_site():
    sites = SiteDetail.objects.filter(is_active=True)
    for site in sites:
        resp = get_site_status(site.site_url)
        if not resp or not resp == 200:
            alert_user(site=site)
        elif site.last_down_time:
            site.last_down_time = 0
            site.status = True
            site.save()
