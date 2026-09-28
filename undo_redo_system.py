from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None

        return self.top.value

    def print_stack(self):
        current = self.top

        if current is None:
            print("Stack is empty.")
            return

        while current is not None:
            print(f"- {current.value}")
            current = current.next


def undo_redo_system():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            action = input(
                "Describe the action (e.g., Insert 'a'): "
            )

            undo_stack.push(action)

            # A new action clears the redo history.
            redo_stack = Stack()

            print(f"Action performed: {action}")

        elif choice == "2":
            action = undo_stack.pop()

            if action is None:
                print("No actions to undo")
            else:
                redo_stack.push(action)
                print(f"Undid action: {action}")

        elif choice == "3":
            action = redo_stack.pop()

            if action is None:
                print("No actions to redo")
            else:
                undo_stack.push(action)
                print(f"Redid action: {action}")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-6.")


if __name__ == "__main__":
    undo_redo_system()
