import time
import numpy as np

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def create_linked_list(values):
    """Create a linked list from a list of values."""
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

def sum_linked_list(head):
    """Sum all values in a linked list."""
    total = 0
    current = head
    while current:
        total += current.value
        current = current.next
    return total

def benchmark(N=1_000_000):
    """Benchmark linked list vs NumPy array summation."""
    data = list(range(N))

    # Linked list benchmark
    linked_head = create_linked_list(data)
    start = time.perf_counter()
    sum_linked_list(linked_head)
    linked_time = time.perf_counter() - start

    # NumPy array benchmark
    arr = np.array(data, dtype=np.int32)
    start = time.perf_counter()
    np.sum(arr)
    numpy_time = time.perf_counter() - start

    print("\n------ Benchmark Results ------\n")
    print(f"Linked List Sum Time: {linked_time:.6f} seconds")
    print(f"NumPy Array Sum Time: {numpy_time:.6f} seconds")
    print(f"Speedup: {linked_time / numpy_time:.2f}x")

if __name__ == "__main__":
    benchmark()
