# [Certbot](https://certbot.eff.org/) - plugin


## Install

```bash
git clone https://github.com/ilupasco/certbot-mdns.git
cd certbot-mdns
python3 setup.py install
```

## Credentials

You need to supply Certbot with your  API credentials, this is an example of how a credentials file can look:

```ini
# API credentials Auth Token by Certbot
# JWT example
mdns_auth_token = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImluZm9AbmljLm1kIiwicm9sZSI6ImRucyIsImRvbWFpbiI6Im5pYy5tZCIsIm5vdGUiOiJ0ZXN0IHRva2VuICIsInR0bCI6eyJkYXlzIjoxfSwiZXhwIjoxNzEzNjEwOTQ4fQ.1ID0LbI4H_Hjei8DAWqG8JkULPhn1tNxtD6mo280NhQ
# AUTH example
mdns_auth_token = 1ID0LbI4H_Hjei8DAWqG8JkULPhn1tNxtD6mo280NhQ
```

## Examples

Simple example for a single domain:

```bash
certbot certonly \
  --authenticator mdns \
  --mdns-credentials ~/.secrets/example1.ini \
  -d example1.com

certbot certonly \
  --authenticator mdns \
  --mdns-credentials ~/.secrets/example2.ini \
  -d example2.com
  
```

Simple example for wildcard domain:

```bash
certbot certonly \
  --authenticator mdns \
  --mdns-credentials ~/.secrets/example.ini \
  -d my.example.com
  -d *.my.example.com
```

Example changing the propagation delay, although you should not have to
adjust it normally:

```bash
certbot certonly \
  --authenticator mdns \
  --mdns-credentials ~/.secrets/example.ini \
  --dns-manager-propagation-seconds 60 \
  -d my.example.com
```
