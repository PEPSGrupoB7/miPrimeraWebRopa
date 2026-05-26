FROM httpd:2.4-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache apr-dev apr-util-dev pcre-dev libxml2-dev \
    lua-dev curl-dev yajl-dev libmaxminddb-dev lmdb-dev

COPY demo.apache.conf /usr/local/apache2/conf/demo.apache.conf
COPY ./static/ /var/www/html
COPY ./ssl/server.crt /usr/local/apache2/conf/ssl/server.crt
COPY ./ssl/server.key /usr/local/apache2/conf/ssl/server.key

RUN echo "Include /usr/local/apache2/conf/demo.apache.conf" \
    >> /usr/local/apache2/conf/httpd.conf

RUN chmod 755 /var \
    && chmod 755 /var/www \
    && chmod -R 755 /var/www/html