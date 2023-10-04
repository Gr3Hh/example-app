## Introduction
This service provides possibility to add user with birthday date in database and get days till birthday by username. 

Usage:  
* **GET** request to `$URL/hello/<username>` return days till birthday if user exist
* **PUT** request to `$URL/hello/<username>` with body `{ "dateOfBirth": "YYYY-MM-DD" }` will add or update existing user.

## Stack
* Framework: FastAPI
* Testing: pytest
* Database: postgresql
* ORM: SQLAlchemy

## Requirements
* poetry
* docker-compose

## Quick Start
1. Install poetry environment: `poetry install`
2. run project: `make up`

## Environment Variables
**POSTGRES_HOST** - database hostname, default: `localhost`  
**POSTGRES_PORT** - database port, default: `5432`  
**POSTGRES_DB** - database name, default `postgres`  
**POSTGRES_USER** - database user, default `postgres`  
**POSTGRES_PASSWORD** - user password, default `postgres`

## List of available operations
The main operations are:  
`make up` - up this application  
`make build_up` - up application with rebuild  
`make stop` - shutdown application  

List of all available commands located at `MakeFile` at the root directory.
