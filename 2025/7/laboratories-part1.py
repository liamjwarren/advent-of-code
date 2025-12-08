class GridCoordinate():
    def __init__(self, x, y, splitter, beam, startingPoint):
        self.x: int = x
        self.y: int = y
        self.splitter: bool = splitter
        self.beam: bool = beam
        self.startingPoint: bool = startingPoint

class Laboratories():
    indexes: int = 0
    startingPoint: GridCoordinate
    grid: list[list[GridCoordinate]] = []
    columns: int = 0
    rows: int = 0
    tachyonBeamSplit: int = 0

    def parse_input(self):
        y = 0
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    x = 0
                    stripped_line = line.strip()
                    row: list[GridCoordinate] = []
                    for char in stripped_line:
                        if char == "^":
                            row.append(GridCoordinate(x, y, True, False, False))
                        elif char == "S":
                            self.startingPoint = GridCoordinate(x, y, False, False, True)
                            row.append(GridCoordinate(x, y, False, False, True))
                        else:
                            row.append(GridCoordinate(x, y, False, False, False))
                        x += 1
                    self.grid.append(row)
                    y += 1
                    self.rows += 1
                self.columns = len(self.grid[0]) if self.grid else 0
        except Exception as e:
            print(f"Exception during parsing input: {e}")

    def process_input(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row): 
               
                # handle start of beam
                if x == self.startingPoint.x and y == self.startingPoint.y:
                    self.grid[y][x].beam = True
                
                # extend beam down - if cell above has beam, current cell gets beam
                if y > 0 and self.grid[y-1][x].beam:
                    # don't extend beam onto splitter, but process the split
                    if self.grid[y][x].splitter:
                        # check bounds before accessing left/right
                        if x > 0 and x < self.columns - 1:
                            self.grid[y][x-1].beam = True
                            self.grid[y][x+1].beam = True
                            self.tachyonBeamSplit += 1
                        continue
                    
                    self.grid[y][x].beam = True
                
    def print_solution(self):
        print(f"The solution is {self.tachyonBeamSplit}")

    def visualize_grid(self):
        """Visualize the grid:
        S = starting point
        ^ = splitter
        | = beam
        . = empty
        """
        for row in self.grid:
            line = ""
            for cell in row:
                if cell.startingPoint:
                    line += "S"
                elif cell.splitter:
                    line += "^"
                elif cell.beam:
                    line += "|"
                else:
                    line += "."
            print(line)
        print()

    def determine_solution(self):
        self.parse_input()
        print("Initial grid:")
        self.visualize_grid()
        self.process_input()
        print("After processing:")
        self.visualize_grid()
        self.print_solution()


if __name__ == "__main__":
    laboratories = Laboratories()
    laboratories.determine_solution()
