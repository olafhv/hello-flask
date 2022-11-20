# Hello cloud native Flask

In this example skeleton Flask application is provided with Prometheus
metrics endpoint.

Steps to take with this repository:

* Fork this repository to your personal GitHub
* Clone the forked repository to your machine
* Obtain sandbox environment from https://dashboard.codemowers.eu/
* Follow the instructions on the page regarding `~/.kube/config` reconfiguration
* Execute the `skaffold dev ...` command provided on the sandbox detailed view
  page to build and deploy the application in the remote cluster sandbox
* Proceed to build your awesome Flask application

# Building and running locally

With vanilla Docker

```
docker build . -t hello-flask:latest
docker run --network host -it hello-flask:latest
```

With `docker-compose`:

```
docker-compose up --build
```
