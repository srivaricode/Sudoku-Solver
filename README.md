# Sudoku-Solver-Graph-Coloring

BLOG POST of original project by [Ishaan Gupta](https://www.github.com/Ishaan97/) - https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072

### My key modifications
* Consistent use of `m=9` to promote variable board size
* Replaced redundant variables with class attributes for reduced coupling between methods.
* Modified `__IsSafe2Color` to iterate through neighbours of vertex `v` instead of entire board, reducing execution time by ~45%. Added `getNeighbours` to `Graph` class.
* Added module `sudoku_board` to fetch random board using [YouDoSudoku](https://www.youdosudoku.com/) API. 
