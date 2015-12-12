FROM sentry:7.7

RUN pip install psycopg2 mysql-python python-memcached redis hiredis nydus
RUN pip install -U sentry==8.0.0rc1
COPY daocloud-links.conf.py /
COPY docker-entrypoint.sh /
EXPOSE 9000
CMD ["/docker-entrypoint.sh"]

