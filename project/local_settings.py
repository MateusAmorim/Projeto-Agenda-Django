# type: ignore
# flake8: noqa

# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
#SECRET_KEY = 'django-insecure-@0z$9fp7cdl8$*toz#xneq9!*op(0mtx^9$d0=!@2ux_ab#+b$'

# DEBUG DEVE SER False em produção
#DEBUG = False

# Seu domínio ou IP devem vir aqui
#ALLOWED_HOSTS = [
#    '34.125.112.163',
#]  # Troque * para seu domínio ou IP

# Config para postgresql
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'projeto_agenda',
#        'USER': 'usuario_agenda',
#        'PASSWORD': 'senha_usuario_agenda',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}