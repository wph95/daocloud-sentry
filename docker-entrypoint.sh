#!/bin/bash
sentry --config=/daocloud-links.conf.py upgrade
sentry --config=/daocloud-links.conf.py celery beat &
sentry --config=/daocloud-links.conf.py celery worker &
exec sentry --config=/daocloud-links.conf.py start
