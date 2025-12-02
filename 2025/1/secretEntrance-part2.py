class DialMovement():
    def __init__(self, direction, steps):
        self.direction: int = direction
        self.steps: int = steps

class SecretEntrance():
    starting_point : int = 50
    current_point: int = starting_point
    password: int = 0
    movements: list[DialMovement] = []


    def parse_input(self):
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    # get rid of the trailing newline to be safe
                    stripped_line = line.strip()
                    direction = stripped_line[0]
                    if(direction == "L"):
                       self.movements.append(DialMovement(-1, int(stripped_line[1:])))
                    else:
                        self.movements.append(DialMovement(1, int(stripped_line[1:])))
        except Exception as e:
            print(f"Exception during parsing input: {e}")


    def determine_password(self):
        self.parse_input()

        for movement in self.movements:
            step_counter: int = 0
            direction = movement.direction
            steps = movement.steps
            for step_counter in range(steps):
                # check if we need to increment the password
                if self.current_point == 0:
                    self.password += 1
                # handle the dial being 0 - 99
                if direction == -1:
                    if self.current_point == 0:
                        self.current_point = 99
                    else:
                        self.current_point -= 1
                else:
                    if self.current_point == 99:
                        self.current_point = 0
                    else:
                        self.current_point += 1

        print(f"The password is {self.password}")

if __name__ == "__main__":
    secretEntrance = SecretEntrance()
    secretEntrance.determine_password()
