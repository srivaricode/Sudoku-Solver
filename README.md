# Sudoku-Solver-Graph-Coloring

BLOG POST of original project - https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072

### Key contributions
* Consistent use of `m=9` to promote variable board size
* Replaced redundant variables with class attributes for reduced coupling between methods.
* Modified `__IsSafe2Color` to iterate through neighbours of vertex `v` instead of entire board, reducing execution time by ~45%. Added `getNeighbours` to `Graph` class.
