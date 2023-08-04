#  1 . Delete the elements in an linked list whose sum is equal to zero.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_zero_sum(head):
    # Helper function to find the cumulative sum of nodes
    def find_cumulative_sum(start_node):
        cumulative_sum = 0
        node = start_node
        while node:
            cumulative_sum += node.value
            yield cumulative_sum
            node = node.next

    # Create a dummy node to handle edge cases where the head is removed
    dummy = Node(0)
    dummy.next = head
    node = dummy

    cumulative_sum_set = set()
    # Find cumulative sums and remove nodes whose sum is in the set
    for cumulative_sum in find_cumulative_sum(node):
        cumulative_sum_set.add(cumulative_sum)

    node = dummy
    # Traverse again and remove nodes whose sum is in the set
    for cumulative_sum in find_cumulative_sum(node):
        node.next = None if cumulative_sum in cumulative_sum_set else node.next
        node = node.next

    return dummy.next


# 2 . Reverse a linked list in groups of given size

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list_in_groups(head, k):
    def reverse_segment(start_node, k):
        prev = None
        curr = start_node
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev, curr

    dummy = Node(0)
    dummy.next = head
    prev_group_tail = dummy

    while prev_group_tail.next:
        kth_node = prev_group_tail
        for i in range(k):
            kth_node = kth_node.next
            if not kth_node and i < k - 1:
                return dummy.next

        next_group_head = kth_node.next

        reversed_head, reversed_tail = reverse_segment(prev_group_tail.next, k)

        prev_group_tail.next = reversed_head
        prev_group_tail = reversed_tail

        prev_group_tail.next = next_group_head

    return dummy.next

def print_linked_list(head):
    node = head
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Original linked list:")
    print_linked_list(head)

    k = 3
    head = reverse_linked_list_in_groups(head, k)

    print(f"Linked list after reversing in groups of {k}:")
    print_linked_list(head)

# 3class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_linked_lists_alternate(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    current1 = head1
    current2 = head2

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    if current2:
        # If the second list is longer, attach the remaining nodes to the end of the first list
        current1.next = current2

    return head1

def print_linked_list(head):
    node = head
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create the first linked list: 1 -> 2 -> 3 -> None
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

    # Create the second linked list: 4 -> 5 -> 6 -> 7 -> 8 -> None
    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(8)

    print("First linked list:")
    print_linked_list(head1)

    print("Second linked list:")
    print_linked_list(head2)

    head1 = merge_linked_lists_alternate(head1, head2)

    print("Merged linked list:")
    print_linked_list(head1)

# 4.  In an array, Count Pairs with given sum.

def count_pairs_with_sum(arr, target_sum):
    # Create a dictionary to store the occurrences of elements in the array
    num_counts = {}

    # Initialize the count of pairs to zero
    pair_count = 0

    # Traverse the array
    for num in arr:
        # Check if the complement (target_sum - num) is present in the dictionary
        complement = target_sum - num
        if complement in num_counts:
            # If the complement is present, add its count to the pair_count
            pair_count += num_counts[complement]

        # Update the count for the current element in the dictionary
        num_counts[num] = num_counts.get(num, 0) + 1

    return pair_count

# Example usage
if __name__ == "__main__":
    # Example array and target sum
    array = [1, 5, 7, -1, 5]
    target_sum = 6

    result = count_pairs_with_sum(array, target_sum)
    print(f"Number of pairs with sum {target_sum}: {result}")


# 5.  Find duplicates in an array 

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example usage:
my_array = [1, 2, 3, 4, 3, 5, 2]
print(find_duplicates(my_array))  # Output: [2, 3]

# 6.  Find the Kth largest and Kth smallest number in an array

def kth_largest_smallest_sort(arr, k):
    arr.sort()
    kth_largest = arr[-k]
    kth_smallest = arr[k - 1]
    return kth_largest, kth_smallest

# Example usage:
my_array = [5, 2, 9, 1, 5, 6]
k = 3
print(kth_largest_smallest_sort(my_array, k))  # Output: (5, 5)


# 7.  Move all the negative elements to one side of the array

def move_negatives_to_one_side(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Find the first positive element from the left
        while left <= right and arr[left] < 0:
            left += 1

        # Find the first negative element from the right
        while left <= right and arr[right] >= 0:
            right -= 1

        # Swap the positive and negative elements
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Example usage:
my_array = [-1, 3, -5, 6, -2, 8, -9]
move_negatives_to_one_side(my_array)
print(my_array)  # Output: [-1, -9, -5, 6, -2, 8, 3]

# 8.  Reverse a string using a stack data structure

def reverse_string(input_str):
    stack = []
    reversed_str = ""

    # Push each character onto the stack
    for char in input_str:
        stack.append(char)

    # Pop characters from the stack to construct the reversed string
    while len(stack) > 0:
        reversed_str += stack.pop()

    return reversed_str

# Example usage:
my_string = "Hello, World!"
reversed_string = reverse_string(my_string)
print(reversed_string)  # Output: "!dlroW ,olleH"

# 9.  Evaluate a postfix expression using stack

def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack.pop()

# Example usage:
postfix_expr = "3 4 + 2 * 7 /"
result = evaluate_postfix(postfix_expr)
print(result)  # Output: 2.0


# 10. Implement a queue using the stack data structure

class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        # Simply push the item onto the enqueue stack
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            # If the dequeue stack is empty, transfer elements from enqueue stack
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # If both stacks are empty, return None
        if not self.stack_dequeue:
            return None

        # Pop the element from the dequeue stack and return it
        return self.stack_dequeue.pop()

    def is_empty(self):
        return not (self.stack_enqueue or self.stack_dequeue)

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: None

