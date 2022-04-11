# Relationship API

## Stack

* gRPC
* REST
* EKS

## Project

### Requirements

* Defined at [`requirements.txt`](requirements.txt) and [`requirements-dev.txt`](requirements-dev.txt)

### Running

#### Locally

* Setup the virtual environment:

```shell
app/scripts/setup-env.sh
```

##### Visual Studio Code

Folder `.vscode` has the required configurations to run the app from the following:

* `Show All Commands` > `View: Show Run and Debug`
  * `Start app`: to run & debug the app
  * `Clear graph`: to clear the graph DB first and then run & debug the app

#### Docker

* Docker has to be installed and running
* Run:

```shell
docker compose up -d
```

* Access <http://localhost:3000> to visualize current nodes and relationships
  * Set host to `'gremlin-server'`
  * Set port to `'8182'`
  * Start with gremlin query `'g.V()'`
  * Execute query
* Install BloomRPC or Postman (newer version) in order to test the gRPC services
* Add proto files to BloomRPC or Postman (using experimental RPC features)
* Use examples provided at [`./examples/`](examples) to test application using BloomRPC or Postman
* Have fun! :)  

## Neptune DB

TBD

### Gremlin

Useful cheatsheets:

* Part 1: <https://dkuppitz.github.io/gremlin-cheat-sheet/101.html>
* Part 2: <https://dkuppitz.github.io/gremlin-cheat-sheet/102.html>

### Data Schema

TBD

### EKS

TBD
