from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        # If the queue is now empty, rear must also be None.
        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        current = self.front

        if current is None:
            print("Queue is empty.")
            return

        while current is not None:
            print(f"- {current.value}")
            current = current.next


def help_desk_system():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            customer = input("Enter customer name: ").strip()

            if customer == "":
                print("Customer name cannot be empty.")
            else:
                queue.enqueue(customer)
                print(f"{customer} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()

            if customer is None:
                print("No customers are waiting.")
            else:
                print(f"Helped: {customer}")

        elif choice == "3":
            customer = queue.peek()

            if customer is None:
                print("No customers are waiting.")
            else:
                print(f"Next customer: {customer}")

        elif choice == "4":
            print("Waiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-5.")


if __name__ == "__main__":
    help_desk_system()
