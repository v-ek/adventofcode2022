from collections import deque


class Monkey:
    monkeys = []
    common_divider = 1

    def __init__(
        self,
        id: int,
        items: list,
        operation: str,
        divider: int,
        true_monkey: int,
        false_monkey: int,
    ):
        self.id = id
        self.items = deque(items)
        self.divider = divider
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.operation = operation
        self._inspect_count = 0
        self.monkeys.append(self)  # Assume monkeys are created in order
        self.increase_common_divider(self.divider)

    def play(self):
        while len(self.items) > 0:
            worry_level = self.items.popleft()
            worry_level = self.operate(worry_level)
            if self.test_is_true(worry_level):
                self.monkeys[self.true_monkey].add_item(worry_level)
            else:
                self.monkeys[self.false_monkey].add_item(worry_level)

            self._inspect_count += 1

    @property
    def inspect_count(self):
        return self._inspect_count

    def operate(self, worry_level):
        operation_parts = self.operation.split("=")[1].strip().split(" ")
        operation = operation_parts[1]
        value = operation_parts[2]
        if operation == "*":
            if value == "old":
                new_worry_level = worry_level * worry_level
            else:
                new_worry_level = worry_level * int(value)
        elif operation == "+":
            if value == "old":
                new_worry_level = worry_level + worry_level
            else:
                new_worry_level = worry_level + int(value)
        return new_worry_level % self.common_divider

    def add_item(self, item):
        self.items.append(item)

    def test_is_true(self, worry_level):
        if worry_level % self.divider == 0:
            return True
        return False

    @classmethod
    def increase_common_divider(cls, divider):
        cls.common_divider *= divider


with open("input_day11.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

curr_monkey_attributes = {}
for line in lines:
    line = line.strip()
    try:
        attribute, value = line.split(":")
        value = value.strip()
        attribute = attribute.strip()
    except ValueError:
        continue
    if attribute.startswith("Monkey"):
        if curr_monkey_attributes != {}:
            Monkey(**curr_monkey_attributes)
            curr_monkey_attributes = {}
        curr_monkey_attributes["id"] = int(attribute.split(" ")[1])
    elif attribute == "Starting items":
        curr_monkey_attributes["items"] = [
            int(item.strip()) for item in value.split(",")
        ]
    elif attribute == "Operation":
        curr_monkey_attributes["operation"] = value
    elif attribute == "Test":
        curr_monkey_attributes["divider"] = int(value.split(" ")[-1].strip())
    elif attribute == "If true":
        curr_monkey_attributes["true_monkey"] = int(value.split(" ")[-1].strip())
    elif attribute == "If false":
        curr_monkey_attributes["false_monkey"] = int(value.split(" ")[-1].strip())
else:
    Monkey(**curr_monkey_attributes)

for idx in range(10000):
    for monkey in Monkey.monkeys:
        monkey.play()

activity_levels = sorted([monkey.inspect_count for monkey in Monkey.monkeys])
print(activity_levels[-1] * activity_levels[-2])
