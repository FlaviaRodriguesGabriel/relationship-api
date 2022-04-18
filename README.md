# Relationship API

<p align="center">
  <img width="auto" height="256" src="./img/logo.png" alt="logo">
</p>

A HTTP server that provides relationship management between PF (natural person) and PJ (legal person) by using a graph database.

<!-- <style>
h1 {
  border-top: 1px solid grey;
}
h2 {
  border-top: 0.5px solid grey;
}
h3 {
  border-top: 0.25px solid grey;
}

body { counter-reset: h2counter; }
h2   { counter-reset: h3counter; }
h3   { counter-reset: h4counter; }
h4   { counter-reset: h5counter; }
h5   { counter-reset: h5counter; }

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}
h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) ". ";
}
h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) ". ";
}
h5::before {
    counter-increment: h5counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) "." counter(h5counter) ". ";
}
h6::before {
    counter-increment: h6counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) "." counter(h5counter) "." counter(h6counter) ". ";
}
</style> -->

## Stack

* 🐍 [Python](http://python.org/)
* 🛠 [Flask](https://flask.palletsprojects.com/)
* 🕸 [EKS](https://aws.amazon.com/eks/)

## Project

### Prerequisites

#### System requirements

* 🐍 Python 3.8 (see [installation guide](https://www.python.org/downloads/))
* 🐍 pip (see [installation guide](https://pip.pypa.io/en/latest/installation/))
* 🐍 virtualenv ([`pip install virtualenv`](https://pypi.org/project/virtualenv/))
* 🐳 Docker (see [installation guide](https://docs.docker.com/engine/install/))

#### App requirements

1. Before installing any requirement, ensure you are using a Python 3.8 environment:
   1. Preferable, start by installing a virtual environment: `virtualenv --python py38 .venv`
   1. Then entering into it: `source .venv/bin/activate`
2. Install all requirements (libraries):
   1. [`app/requirements.txt`](app/requirements.txt): for the app to be able to run
   2. [`app/requirements-dev.txt`](app/requirements-dev.txt): for a developer to test, change and commit code are defined

```bash
pip install -r app/requirements.txt
# or
pip install -r app/requirements-dev.txt  # already installs what is in `app/requirements.txt` too
```

#### Optional tools

* 🚀 [Postman](https://www.postman.com): for HTTP requests testing

### Quickstart

#### Running the app

1. `docker compose -f docker-compose.yml -p relationship-api up -d` to run all required services (i.e. Gremlin DB server and other tools)
1. Run the app by either:
   1. [`scripts/run-server.sh`](scripts/run-server.sh): executing the script
   1. `python -m app/src`: manually executing the module (ensure you are using a Python 3.8 environment from[follow app requiments guideline above](#app-requirements))
   1. `Visual Studio Debug/Run`: folder [`.vscode`](.vscode) has some configurations

#### Visualizing the app results

1. Access <http://localhost:3000> to visualize current vertices and edges
   1. Set host to `gremlin-server`
   1. Set port to `8182`
   1. Start with gremlin query (e.g. `g.V()`)
   1. Execute the query
2. Use Postamn's examples provided at [`./examples`](./examples) to test app's HTTP server
3. Have fun! 🎉

## Resources

### Gremlin

* Cheatsheet:
  * Part 1/2: <https://dkuppitz.github.io/gremlin-cheat-sheet/101.html>
  * Part 2/2: <https://dkuppitz.github.io/gremlin-cheat-sheet/102.html>

### Neptune DB

TBD

### Gremlin

### Data Schema

TBD

### EKS

TBD
