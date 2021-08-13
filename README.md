# Setup

#### Create local env file

Just run `make test_env`


#### Build containers

`docker-compose -f docker-compose-dev.yml build`

#### Before running project

- Create local env file
- Build containers
- Run project

#### Run project

`docker-compose -f docker-compose-dev.yml up`


#### When project is running

- Apply db migrations `make migrations`
- Create superuser `make test_user`. After that you will be able to login into Admin
- Be happy

#### Create new app

`make app name=<app_name>`

### Project description

This is simple project just to demonstrate basic concept of Django.

- You are able to see Django Admin and create some articles in DB.
- You can search recently added articles on /articles/search/ page. 
And see the results on /articles/results/ page.

#### All commands you can find in `Makefile`
