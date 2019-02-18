FROM python:3.6-alpine

ENV WORKDIR /casepro
WORKDIR $WORKDIR

RUN apk add --no-cache varnish wget gettext git
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache postgresql-dev nodejs nodejs-npm
RUN apk add --no-cache supervisor

COPY varnish.default.vcl /etc/varnish/default.vcl
COPY pip-freeze.txt .
COPY package.json .

RUN pip install -r pip-freeze.txt
RUN npm install
RUN npm install -g less coffeescript

COPY . .

EXPOSE 8000
EXPOSE 8080

RUN chmod +x ./entrypoint.sh
RUN chmod +x ./start-app.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["supervisor"]
