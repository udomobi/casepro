FROM ilha/rapidpro-base:base

ENV WORKDIR /casepro
WORKDIR $WORKDIR

RUN apt-get update && apt-get install -y \
    apt-utils \
    varnish \
    wget \
    gettext \
    python3.6 \
    python3.6-dev \
    python3.6-minimal \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6

COPY varnish.default.vcl /etc/varnish/default.vcl
COPY pip-freeze.txt .
COPY package.json .

RUN pip install -r pip-freeze.txt
RUN npm install

COPY . .

EXPOSE 8000
EXPOSE 8080

RUN chmod +x ./entrypoint.sh
RUN chmod +x ./start-app.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["supervisor"]
