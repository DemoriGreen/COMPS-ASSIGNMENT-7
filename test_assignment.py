from node import Node
from undo_redo_system import Stack
from help_desk_queue import Queue


def test_node():
    node = Node("Test")

    assert node.value == "Test"
    assert node.next is None

    print("Node test passed.")


def test_stack():
    stack = Stack()

    # Edge case: empty stack
    assert stack.pop() is None
    assert stack.peek() is None

    # Interaction 1
    stack.push("Action 1")

    # Interaction 2
    stack.push("Action 2")

    # Interaction 3
    stack.push("Action 3")

    # Interaction 4: peek
    assert stack.peek() == "Action 3"

    # Interaction 5: pop
    assert stack.pop() == "Action 3"

    # Additional interaction
    assert stack.pop() == "Action 2"
    assert stack.peek() == "Action 1"

    # Empty again
    assert stack.pop() == "Action 1"
    assert stack.pop() is None

    print("Stack tests passed.")


def test_queue():
    queue = Queue()

    # Edge cases: empty queue
    assert queue.dequeue() is None
    assert queue.peek() is None

    # Interaction 1
    queue.enqueue("Jordan")

    # Interaction 2
    queue.enqueue("Taylor")

    # Interaction 3
    queue.enqueue("Morgan")

    # Interaction 4: peek
    assert queue.peek() == "Jordan"

    # Interaction 5: dequeue
    assert queue.dequeue() == "Jordan"

    # Verify FIFO order
    assert queue.peek() == "Taylor"
    assert queue.dequeue() == "Taylor"
    assert queue.dequeue() == "Morgan"

    # Queue should now be empty
    assert queue.peek() is None
    assert queue.dequeue() is None

    # Verify front/rear both reset
    assert queue.front is None
    assert queue.rear is None

    print("Queue tests passed.")


def test_stack_redo_behavior():
    undo_stack = Stack()
    redo_stack = Stack()

    undo_stack.push("Insert A")
    undo_stack.push("Insert B")

    # Undo B
    action = undo_stack.pop()
    redo_stack.push(action)

    assert action == "Insert B"
    assert undo_stack.peek() == "Insert A"
    assert redo_stack.peek() == "Insert B"

    # Redo B
    action = redo_stack.pop()
    undo_stack.push(action)

    assert action == "Insert B"
    assert undo_stack.peek() == "Insert B"
    assert redo_stack.peek() is None

    print("Undo/redo behavior test passed.")


if __name__ == "__main__":
    test_node()
    test_stack()
    test_queue()
    test_stack_redo_behavior()

    print("\nAll tests passed!")
