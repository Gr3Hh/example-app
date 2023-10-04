# General information

## Application
The application is located at `./application` directory and contain all required instruments for get it up locally and test it.  
* `./application/app/README.md` includes information about using the application.
* `./application/app/main.py` etnrypoint of application.  
* `./application/app/tests` directory contains tests for the application.  

## CI part
* Configuration file for CircleCI located at `./application/app/.circleci/config.yaml`

This file contains a pipeline for testing non-master branches and testing and building the master branch.  
* testing is done using docker-compose and utilities such as: `flake8, safety, pip-licenses, bandit, pytest`. All these utilities are included in the poetry dev group.
* build occurs using orbs from google cloud provider after passing all tests. This image is tagged with the name of the branch and an unique pipeline number, after which it is placed in the google container registry.

## Deployment
Deployment occurs using helm charts.
* `./application/helm-charts/postgresql` Using helm, simple installation of the postgresql database in the cluster. The best solution is to use the database as a service from a provider.
* `./application/helm-charts/app` helm chart made for use via ArgoCD.  
The migration task `alembic upgrade head` will run before the main deployment.  

Some explanations for this task:
1. During deployment, before applying migration, I need to make a backup of the database.
2. Liveness and other probes must be for a specific healthcheck for their reliability.
3. For image tags I use latest, which is definitely not good practice.

all these things mentioned above were done simply because this is homework and not a production environment.

### Without downtime and stable work

For this purpose the following tools were used:
* update strategy `RollingUpdate`
* soft `podAntiAffinity` to place pods on different nodes in case of some kind of disaster with node
* `PodDisruptionBudget` again in case of some unexpected situation or cluster update
