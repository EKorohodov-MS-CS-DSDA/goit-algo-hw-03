# Recursion. Homework 3. Task 3.

class Tower:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return str(self.name) + ": " + str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        raise IndexError("Stack is empty")


def hanoi(n, from_tower, helper_tower, to_tower):
    if n == 1:
        print(f"Move disk {n} from tower {from_tower} to tower {to_tower}.")
        from_tower.pop()
        to_tower.push(n)
        return
    hanoi(n - 1, from_tower, to_tower, helper_tower)
    print(f"Move disk {n} from tower {from_tower} to tower {to_tower}.")
    from_tower.pop()
    to_tower.push(n)
    hanoi(n - 1, helper_tower, from_tower, to_tower)

def main():
    N = 5

    tower_A = Tower("A")
    tower_B = Tower("B")
    tower_C = Tower("C")

    for i in range(N, 0, -1):
        tower_A.push(i)

    print(f"Initial state: {tower_A}, {tower_B}, {tower_C}")
    hanoi(N, tower_A, tower_B, tower_C)
    print(f"Final state: {tower_A}, {tower_B}, {tower_C}")

if __name__ == '__main__':
    main()
