# Deployment Configuration Report

## Introduction

This document provides instructions for configuring the web server to support HTTPS and secure the Django application deployment. It includes steps for setting up SSL/TLS certificates and configuring the web server for secure communication.

## Nginx Configuration

1. **Install Nginx**:
   Ensure Nginx is installed on your server.

   ```bash
   sudo apt update
   sudo apt install nginx

2. **Obtain SSL Certificates**: Use Certbot to obtain SSL certificates.

```
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

3. **Configure Nginx for HTTPS**: Update your Nginx server block configuration file.
```
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'AES256+EECDH:AES256+EDH:!aNULL:!MD5:!RC4';
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

4. Reload Nginx Configuration:
```
sudo systemctl reload nginx
```