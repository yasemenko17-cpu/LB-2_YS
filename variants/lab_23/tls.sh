#!/usr/bin/env bash
mkdir -p certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/blog.key \
  -out certs/blog.crt \
  -subj "/CN=blog.lab.test" \
  -addext "subjectAltName=DNS:blog.lab.test,IP:127.0.0.1"
chmod 600 certs/blog.key