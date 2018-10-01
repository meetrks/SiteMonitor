from django.conf import settings

from twilio.rest import Client

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


def send_sms(users, site):
    site_name = site.site_name
    site_url = site.site_url
    for user in users:
        if user.mobile:
            client.messages.create(
                to=user.mobile,
                from_=settings.TWILIO_PHONE_NUMBER,
                body="You site is down. Site Name- " + site_name + ", Site URL- " + site_url
            )