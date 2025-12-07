class Lobby():
    jottage_sum: int = 0
    banks: list[str] = []

    def parse_input(self):
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    self.banks.append(line.strip())
        except Exception as e:
            print(f"Exception during parsing input: {e}")
    
    def process_input(self):
        for bank in self.banks:
            first_digit : int = 0
            first_digit_index : int = -1
            second_digit : int = 0

            # find the first digit
            for index in range(len(bank)-1):
                current_index_int = int(bank[index])
                if current_index_int > first_digit:
                    first_digit = current_index_int
                    first_digit_index = index

            # find the second digit
            for index in range(first_digit_index + 1, len(bank)):
                current_index_int = int(bank[index])
                if current_index_int > second_digit:
                    second_digit = current_index_int
            
            bank_jottage = int(str(first_digit) + str(second_digit))
            self.jottage_sum += bank_jottage

    def print_solution(self):
        print(f"The solution is {self.jottage_sum}")

    def determine_solution(self):
        self.parse_input()
        self.process_input()
        self.print_solution()

if __name__ == "__main__":
    lobby = Lobby()
    lobby.determine_solution()
