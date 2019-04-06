# Artificial-Intelligence---The-PacMan-Projects

This project work is a part of Artificial Intelligence coursework at the [University of Oulu](http://www.oulu.fi/university/).
Link: https://weboodi.oulu.fi/oodi/opintjakstied.jsp?Kieli=6&Tunniste=521495A&html=1

This project is based on The Pac-Man projects developed by John DeNero, Dan Klein, and Pieter Abbeel at UC Berkeley. Link: http://ai.berkeley.edu/project_overview.html

We implement artifical intelligence of agents in the [Pacman](https://en.wikipedia.org/wiki/Pac-Man) world. Use commands below to run the client with the desired algorithm.

## Getting started

Follow the instructions below to get started.

### Prerequisites

The code is written in [Python 2.7](https://www.python.org/download/releases/2.7/).


## Running the program

You should be able to play a game of Pac-Man by typing the following at the command line:

```
$ python pacman.py
```

## Built with

* [Python 2.7](https://www.python.org/download/releases/2.7/)


## Search

- [x] Depth First Search

```
$ python pacman.py -l tinyMaze -p SearchAgent
$ python pacman.py -l mediumMaze -p SearchAgent
$ python pacman.py -l bigMaze -z .5 -p SearchAgent
```

- [x] Breadth First Search

```
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

- [x] Uniform Cost Search

```
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

- [x] A* Search

```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## Multi-Agent Search

- [x] Reflex Agent

```
$ python pacman.py -p ReflexAgent -l testClassic
$ python pacman.py --frameTime 0 -p ReflexAgent -k 1
$ python pacman.py --frameTime 0 -p ReflexAgent -k 2
```

- [x] Minimax

```
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
$ python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
```

- [x] Alpha-Beta Pruning

```
$ python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
$ python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
```

- [x] Expectimax

```
$ python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
$ python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```

## Evaluation

These are the command for obtaining evaluation results.

#### Open Classic Maze

```
$ python pacman.py -p ReflexAgent -l openClassic -q -n 10
$ python pacman.py -p MinimaxAgent -l openClassic -a depth=3 -q -n 10
$ python pacman.py -p AlphaBetaAgent -l openClassic -a depth=3 -q -n 10
$ python pacman.py -p ExpectimaxAgent -l openClassic -a depth=3 -q -n 10
```

#### Small Classic Maze

```
$ python pacman.py -p ReflexAgent -l smallClassic -q -n 10
$ python pacman.py -p MinimaxAgent -l smallClassic -a depth=3 -q -n 10
$ python pacman.py -p AlphaBetaAgent -l smallClassic -a depth=3 -q -n 10
$ python pacman.py -p ExpectimaxAgent -l smallClassic -a depth=3 -q -n 10
```

#### Medium Classic Maze

```
$ python pacman.py -p ReflexAgent -l mediumClassic -q -n 10
$ python pacman.py -p MinimaxAgent -l mediumClassic -a depth=3 -q -n 10
$ python pacman.py -p AlphaBetaAgent -l mediumClassic -a depth=3 -q -n 10
$ python pacman.py -p ExpectimaxAgent -l mediumClassic -a depth=3 -q -n 10
```

#### Tricky Classic Maze

```
$ python pacman.py -p ReflexAgent -l trickyClassic -q -n 10
$ python pacman.py -p MinimaxAgent -l trickyClassic -a depth=3 -q -n 10
$ python pacman.py -p AlphaBetaAgent -l trickyClassic -a depth=3 -q -n 10
$ python pacman.py -p ExpectimaxAgent -l trickyClassic -a depth=3 -q -n 10
```

#### Minimax Classic Maze

```
$ python pacman.py -p ReflexAgent -l minimaxClassic -q -n 10
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=3 -q -n 10
$ python pacman.py -p AlphaBetaAgent -l minimaxClassic -a depth=3 -q -n 10
$ python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3 -q -n 10
```

#### Trapped Classic Maze

```
$ python pacman.py -p ReflexAgent -l trappedClassic -q -n 10
$ python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3 -q -n 10
$ python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
$ python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```

## Author

* **Md Shariful Alam** - [Shariful](https://github.com/Shourov1)

## Acknowledgments

* [The UniOulu AI course and its teachers](https://noppa.oulu.fi/noppa/kurssi/521495a/)
* [The Berkeley AI course](http://ai.berkeley.edu/home.html) - For providing the original materials!
* [The University of Oulu](http://www.oulu.fi/university/) - For providing this awesome course!
