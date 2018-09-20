from django.utils.crypto import get_random_string

ALLOWED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def generate_short_id(id_length=8):
    return get_random_string(length=id_length, allowed_chars=ALLOWED_CHARS)
