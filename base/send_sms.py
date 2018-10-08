from twilio.rest import Client

from settings.models import TwilioSetting

twilio_obj = TwilioSetting.objects.first()
client = Client(twilio_obj.account_sid, twilio_obj.auth_token) if twilio_obj else None


def send_sms(users, site):
    site_name = site.site_name
    site_url = site.site_url
    for user in users:
        if user.mobile and client:
            client.messages.create(
                to=user.mobile,
                from_=twilio_obj.phone_number,
                body="You site is not responding. Site Name- " + site_name + ", Site URL- " + site_url
            )
