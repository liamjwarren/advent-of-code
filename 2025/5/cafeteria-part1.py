
class Cafeteria():
    freshIngredientRanges = []  # List of (start, end) tuples
    ingredientIDsToCheck = []
    availableFreshIngredient: int = 0

    def parse_input(self):
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    stripped_line = line.strip()

                    # handle fresh ingredient ranges (inclusive)
                    if '-' in stripped_line:
                        start, end = map(int, stripped_line.split('-'))
                        self.freshIngredientRanges.append((start, end))
                        continue

                    # handle divider line
                    if stripped_line == '':
                        continue

                    # at this point it is the list of ingredients to check
                    self.ingredientIDsToCheck.append(int(stripped_line))
        except Exception as e:
            print(f"Exception during parsing input: {e}")

    def process_input(self):
        for id in self.ingredientIDsToCheck:
            if any(start <= id <= end for (start, end) in self.freshIngredientRanges):
                self.availableFreshIngredient += 1

    def print_solution(self):
        print(f"The solution is {self.availableFreshIngredient}")

    def determine_solution(self):
        self.parse_input()
        self.process_input()
        self.print_solution()


if __name__ == "__main__":
    cafeteria = Cafeteria()
    cafeteria.determine_solution()
