import re

RE_EMAIL = re.compile(r'[^@]+@[^@]+\.[^@]')


def email_parse(email_address):
    if RE_EMAIL.match(email_address) is not None:
        a = re.split(r'@', email_address)
        dict_email = {'username': a[0], 'domain': a[1]}
        return dict_email
    else:
        raise ValueError(f'wrong email: {email_address}')


print(email_parse('someone@geekbrain.ru'))
