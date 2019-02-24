import time

from celery import shared_task

from base.send_sms import send_sms
from base.utils import get_site_status
from members.models import MemberDirectory
from monitor.models import SiteDetail
from roles.models import Role


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
