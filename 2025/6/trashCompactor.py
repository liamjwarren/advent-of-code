
class TrashCompactor():
    grandTotal: int = 0
    columns = []
    operators = []
    grandTotal = 0

    def parse_input(self):
        with open('input.txt', 'r') as file:
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue

                parts = stripped.split()

                if parts[0] in ('*', '+'):
                    self.operators = parts
                else:
                    if not self.columns:
                        self.columns = [[] for _ in range(len(parts))]
                    for i, num in enumerate(parts):
                        self.columns[i].append(int(num))

    def process_input(self):
        for col, op in zip(self.columns, self.operators):
            if op == '*':
                col_result = 1
                for num in col:
                    col_result *= num
            else:
                col_result = sum(col)
            self.grandTotal += col_result

    def print_solution(self):
        print(f"The solution is {self.grandTotal}")

    def determine_solution(self):
        self.parse_input()
        self.process_input()
        self.print_solution()


if __name__ == "__main__":
    trashCompactor = TrashCompactor()
    trashCompactor.determine_solution()
