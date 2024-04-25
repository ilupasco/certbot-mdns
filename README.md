# [Certbot](https://certbot.eff.org/) - plugin


## Install

```bash
git clone https://github.com/ilupasco/certbot-mdns.git
cd certbot-mdns
python3 setup.py install
```
or
```bash
wget https://github.com/ilupasco/certbot-mdns/raw/main/dist/certbot_mdns-1.0.1-py3-none-any.whl
pip3 install -U certbot_mdns-1.0.1-py3-none-any.whl
```

## Credentials

You need to supply Certbot with your  API credentials, this is an example of how a credentials file can look:

```ini
# API credentials Auth Token by Certbot
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
