# Loans Site

## Introduction

This app simulates a site to request loans, along with an administration site to edit/delete registered loans.

## Running vlidation API

To validate loans, it is necessary to hit an endpoint that requires credentials. Docker will look for these credentials in .env

- Create a file .env in the root directory, see .example.env
- Replace correctPassword with the required credential. 

## Running the app

foo@bar:rootdir/\$ docker-compose build

foo@bar:rootdir/\$ docker-compose up

## Accessing the site:
- Loans application form is at localhost:8000 
- Login site is at localhost:8000/accounts/login
- Loans list (only accessible for registered users) is at localhost:8000/accounts/loans

## Registered users
- A super user admin (password admin) is created when the container is created. This user can access the custom administration site. 


## Prrequisites
- docker
- docker-compose