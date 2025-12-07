class GridCoordinate():
    def __init__(self, x, y, rollOfPaper):
        self.x: int = x
        self.y: int = y
        self.rollOfPaper: bool = rollOfPaper


class PrintingDepartment():
    indexes: int = 0
    grid: list[GridCoordinate] = []
    columns: int = 0
    rows: int = 0
    accessibleRollsOfPaper: int = 0

    def parse_input(self):
        y = 0
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    x = 0
                    stripped_line = line.strip()
                    for char in stripped_line:
                        if char == "@":
                            self.grid.append(GridCoordinate(x, y, True))
                        else:
                            self.grid.append(GridCoordinate(x, y, False))
                        x += 1
                    y += 1
                    self.rows += 1
                    self.columns += 1
        except Exception as e:
            print(f"Exception during parsing input: {e}")

    def process_input(self):
        for index in self.grid:
            adjacentPaperRolls: int = 0

            # skip processing if the current spot does not have a paper roll in it
            if index.rollOfPaper == False:
                continue

            for coordinate in self.grid:
                # check (-1, 1)
                if coordinate.x == index.x - 1 and coordinate.y == index.y + 1 and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (0,1)
                if coordinate.x == index.x and coordinate.y == index.y + 1 and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (1,1)
                if coordinate.x == index.x + 1 and coordinate.y == index.y + 1 and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (-1,0)
                if coordinate.x == index.x - 1 and coordinate.y == index.y and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (1,0)
                if coordinate.x == index.x + 1 and coordinate.y == index.y and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (-1,-1)
                if coordinate.x == index.x - 1 and coordinate.y == index.y - 1 and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (0,-1)
                if coordinate.x == index.x and coordinate.y == index.y - 1 and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

                # check (1,-1)
                if coordinate.x == index.x + 1 and coordinate.y == index.y - 1 and coordinate.rollOfPaper:
                    adjacentPaperRolls += 1

            if adjacentPaperRolls < 4:
                self.accessibleRollsOfPaper += 1

    def print_solution(self):
        print(f"The solution is {self.accessibleRollsOfPaper}")

    def determine_solution(self):
        self.parse_input()
        self.process_input()
        self.print_solution()


if __name__ == "__main__":
    printingDepartment = PrintingDepartment()
    printingDepartment.determine_solution()
