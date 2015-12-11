FROM sentry:7.7

COPY daocloud-links.conf.py /
COPY docker-entrypoint.sh /
EXPOSE 9000
CMD ["/docker-entrypoint.sh"]

