# Relationship API

## Stack:
* gRPC
* REST
* EKS

## Project
### Requirements
* Defined @ requirements.txt and requirements-dev.txt

### Running
* Docker has to be installed and running
* Run 'docker compose up -d'
* Access http://localhost:3000 to visualize current nodes and relationships
    * Set host to 'gremlin-server'
    * Set port to '8182'
    * Start with gremlin query 'g.V()'
    * Execute query
* Run application using Visual Studio Code
    * Folder '.vscode' has some configurations
* Install BloomRPC or Postman (newer version) in order to test the gRPC services
* Add proto files to BloomRPC or Postman (using experimental RPC features)
* Use examples provided @ './examples' to test application using BloomRPC or Postman
* Have fun :)  

## Neptune DB
TBD

### Gremlin
Useful cheatsheets:
* Part 1: https://dkuppitz.github.io/gremlin-cheat-sheet/101.html
* Part 2: https://dkuppitz.github.io/gremlin-cheat-sheet/102.html

### Data Schema
TBD

### EKS
TBD