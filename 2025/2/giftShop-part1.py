class IDRange():
    def __init__(self, start, end):
        self.start: int = start
        self.end: int = end

class GiftShop():
    invalid_ids_sum: int = 0
    id_ranges: list[IDRange] = []

    def parse_input(self):
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    # get rid of the trailing newline to be safe
                    stripped_line = line.strip()
                    parsed_lines = stripped_line.split(',')
                    for parsed_line in parsed_lines:
                        parsed_ids = parsed_line.split('-')
                        self.id_ranges.append(IDRange(parsed_ids[0], parsed_ids[1]))
        except Exception as e:
            print(f"Exception during parsing input: {e}")

    def process_input(self):
        for id_range in self.id_ranges:
            for id in range(int(id_range.start), int(id_range.end)+1):
                if len(str(id)) % 2 == 0:
                    string_id = str(id)
                    middle_index = int(len(str(id))/2)
                    first_sequence = string_id[:middle_index]
                    second_sequence = string_id[middle_index:]
                    if first_sequence == second_sequence:
                        self.invalid_ids_sum += id

    def print_solution(self):
        print(f"The solution is {self.invalid_ids_sum}")

    def determine_solution(self):
        self.parse_input()
        self.process_input()
        self.print_solution()

if __name__ == "__main__":
    giftShop = GiftShop()
    giftShop.determine_solution()
