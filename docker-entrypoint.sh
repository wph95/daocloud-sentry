#!/bin/bash
sentry --config=/daocloud-links.conf.py upgrade
exec sentry --config=/daocloud-links.conf.py start
exec sentry --config=/daocloud-links.conf.py celery beat
exec sentry --config=/daocloud-links.conf.py celery worker
