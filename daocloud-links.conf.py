import os
postgres = os.getenv('SENTRY_POSTGRES_HOST') or (os.getenv('POSTGRESQL_PORT_5432_TCP_ADDR') and 'postgres')
mysql = os.getenv('SENTRY_MYSQL_HOST') or (os.getenv('MYSQL_PORT_3306_TCP_ADDR') and 'mysql')
redis = os.getenv('SENTRY_REDIS_HOST') or (os.getenv('REDIS_PORT_6379_TCP_ADDR') and 'redis')


if postgres:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': (
                os.getenv('SENTRY_DB_NAME')
                or os.getenv('POSTGRESQL_INSTANCE_NAME')
                or 'postgres'
            ),
            'USER': (
                os.getenv('SENTRY_DB_USER')
                or os.getenv('POSTGRESQL_USERNAME')
                or 'postgres'
            ),
            'PASSWORD': (
                os.getenv('SENTRY_DB_PASSWORD')
                or os.getenv('POSTGRESQL_PASSWORD')
                or ''
            ),
            'HOST':  postgres,
            'PORT': (
                os.getenv('POSTGRESQL_PORT_5432_TCP_PORT')
                or '5432'
            ),
            'OPTIONS': {
                'autocommit': True,
            },
        },
    }
elif mysql:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': (
                os.getenv('SENTRY_DB_NAME')
                or os.getenv('MYSQL_INSTANCE_NAME')
                or ''
            ),
            'USER': (
                os.getenv('SENTRY_DB_USER')
                or os.getenv('MYSQL_USERNAME')
                or 'root'
            ),
            'PASSWORD': (
                os.getenv('SENTRY_DB_PASSWORD')
                or os.getenv('MYSQL_PASSWORD')
                or ''
            ),
            'HOST': mysql,
            'PORT': (
                os.getenv('SENTRY_MYSQL_PORT')
                or os.getenv('MYSQL_PORT_3306_TCP_PORT')
                or ''
            ),
        },
    }



SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': 'localhost',
            'port': '6379',
            'db': '0'
        },
    },
}
BROKER_URL = 'redis://'+ 'localhost:6379' + '/0'


SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

# This file is just Python, with a touch of Django which means
# you can inherit and tweak settings to your hearts content.

# You should not change this setting after your database has been created
# unless you have altered all schemas first
SENTRY_USE_BIG_INTS = True

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

###########
# General #
###########

# The administrative email for this installation.
# Note: This will be reported back to getsentry.com as the point of contact. See
# the beacon documentation for more information. This **must** be a string.

# SENTRY_ADMIN_EMAIL = 'your.name@example.com'
SENTRY_ADMIN_EMAIL = os.getenv('SENTRY_ADMIN_EMAIL')

# Instruct Sentry that this install intends to be run by a single organization
# and thus various UI optimizations should be enabled.
SENTRY_SINGLE_ORGANIZATION = True
# Buffers, Quotas, TSDB




SENTRY_CACHE = 'sentry.cache.redis.RedisCache'


CELERY_ALWAYS_EAGER = False


###############
# Rate Limits #
###############

# Rate limits apply to notification handlers and are enforced per-project
# automatically.

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

##################
# Update Buffers #
##################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

##########
# Quotas #
##########

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

########
# TSDB #
########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

################
# File storage #
################

# Any Django storage backend is compatible with Sentry. For more solutions see
# the django-storages package: https://django-storages.readthedocs.org/en/latest/

SENTRY_FILESTORE = 'django.core.files.storage.FileSystemStorage'
SENTRY_FILESTORE_OPTIONS = {
    'location': '/tmp/sentry-files',
}

##############
# Web Server #
##############

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = os.getenv('SENTRY_REDIS_HOST')  # No trailing slash!

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# header and uncomment the following settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    # 'workers': 3,  # the number of gunicorn workers
    # 'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

###############
# Mail Server #
###############

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

# The email address to send on behalf of
SERVER_EMAIL = os.getenv('SERVER_EMAIL')

# If you're using mailgun for inbound mail, set your API key and configure a
# route to forward to /api/hooks/mailgun/inbound/

SECRET_KEY = os.getenv('SECRET_KEY')
