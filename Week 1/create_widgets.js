// From user krishnab on StackOverflow, June 2018.
// Published under CC-BY SA 4.0
// https://stackoverflow.com/a/50921391

window.findCellIndicesByTag = function findCellIndicesByTag(tagName) {
  return (Jupyter.notebook.get_cells()
    .filter(
      ({metadata: {tags}}) => tags && tags.includes(tagName)
    )
    .map((cell) => Jupyter.notebook.find_cell_index(cell))
  );
};

window.runSolutionCells = function runSolutionCells() {
    var c = window.findCellIndicesByTag('solution_cell');
    Jupyter.notebook.execute_cells(c);
};