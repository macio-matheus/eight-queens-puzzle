## Eight queens puzzle

Challenge of the eight queens solved with local search algorithm and basic genetic algorithm

## Tech
```sh
- Python 3.6
- Deap (https://deap.readthedocs.io)
- Search algorithms (Hill climbing)
- Genetic Algorithm
```

## eaSimple (Deap)

Simplest evolutionary algorithm.

## Hill climbing algorithm (pseudcode) 

Hill climbing algorithm is a mathematical optimization technique which belongs to the family of local search.

![Architecture](https://raw.githubusercontent.com/macio-matheus/eight-queens-puzzle/master/imgs/hill_climb.png)

## Build and deploy using Docker

In order to execute the application, it is necessary to perform the build of the docker compose, done that, the application can already be executed with the compose up.

```sh
cd eight-queens-puzzle
docker-compose build
```

Run application environment

```sh
cd eight-queens-puzzle
docker-compose up -d
```

Entering the container and run algorithm

```sh
docker exec -it eight_queens bash
python -m eight-queen-puzzle
```
