# Deploy

This is short instruction how to deploy django app with aws, nginx, docker, and gunicorn.

1. the scheme:

    `browser (http client) > server (hard) > web server (nginx) > gunicorn > django`

2. Launch aws instance, configure security group to allow access for 22 port (ssh), 80 and 433 (http and https);
3. Connect to aws instance;
    
    `ssh ubuntu@<ip>`
4. install packages:
```
apt-get update
apt-get install nginx
```
5. install docker (from official docs)
6. generate private ssh key on the server, add it to your github account, clone repo into `/var/apps/<project_name>/src`
7. nginx config:
```
server {
    charset utf-8;

    server_name 3.68.110.151;

    client_max_body_size 50m;
    keepalive_timeout 5;

    # GZIP
    gzip on;
    gzip_disable "msie6";
    gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/javascript;

    location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header    Host                    $http_host;
            proxy_set_header    User-Agent              $http_user_agent;
            proxy_set_header    X-Real-IP               $remote_addr;
            proxy_set_header    X-Forwarded-For         $proxy_add_x_forwarded_for;
            proxy_set_header    X-Forwarded-Proto       $scheme;
    }
    location /media/ {
            alias /var/apps/trello/media/;
            expires 30d;
    }
    location /static/ {
            alias /var/apps/trello/static/;
            expires 30d;
    }
}
```
Place it into '/etc/nginx/site-available/<project_name>'
8. create sublink to sites-enabled:
   `ln -s /etc/nginx/site-available/<project_name> /etc/nginx/site-enabled/<project_name>`
9. build docker:
```
cd /var/apps/<proj>/src/
docker-compose -f docker-compose-prod.yml up --build -d 
```
13. Profit!