FROM owasp/modsecurity-crs:3.3-apache

COPY demo.apache.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf
COPY ./static/ /var/www/html
COPY ./ssl/server.crt /usr/local/apache2/conf/ssl/server.crt
COPY ./ssl/server.key /usr/local/apache2/conf/ssl/server.key

RUN apt-get update && apt-get install -y libapache2-mod-evasive && \
    mkdir -p /var/log/mod_evasive && \
    chmod 777 /var/log/mod_evasive

RUN chmod 644 /usr/local/apache2/conf/ssl/server.crt \
    && chmod 644 /usr/local/apache2/conf/ssl/server.key \
    && chmod -R 755 /var/www/html