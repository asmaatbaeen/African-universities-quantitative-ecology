#  African-universities-quantitative-ecology

## 1. Getting Started

 I use [poetry](https://python-poetry.org/) to manage packages - so install poetry first if you haven't already.

To install dependencies, do:

```
$ poetry shell
$ poetry install
```

 
### Run

To start the scheduler service and tile matching/indexing, run:
```
$ poetry run service
```

At this point, you may still see errors, because you need to set up secret environment variables, as well as run the tasseograph database locally.

To start the traffic API, run:
```
poetry run api
``` 

## 2. Scripts
This section covers scripts that used to run the notebook to produce the various graph  outputs  from the presented data
config.ini --- environmental varaiables 
	the patb the to the shape file of Africa map
 
```
data
├── graph
├── gtfs
│   
All paths under `data` are ignored by default, so you may slightly different content depending what scripts you've run so far.


 