# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)

    return pairs


## Q2. Write a program to reverse an array in place? In place means you cannot create a new array.
#   You have to update the original array.

def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]

        # Move the pointers towards the center of the array
        left += 1
        right -= 1



## Write a program to check if two strings are a rotation of each other?

def are_strings_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    # Concatenate str1 with itself to form a new string
    concat_str = str1 + str1

    # Check if str2 is a substring of concat_str
    if str2 in concat_str:
        return True
    else:
        return False




## Write a program to print the first non-repeated character from a string?


def first_non_repeated_character(string):
    char_count = {}

    # Count the occurrences of each character in the string
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char

    return None  # If no non-repeated character is found


##  Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)




## Read about infix, prefix, and postfix expressions. Write a program to convert postfix 
# to prefix expression.


def is_operator(char):
    return char in {'+', '-', '*', '/'}

def postfix_to_prefix(postfix_expr):
    stack = []
    for char in postfix_expr.split():
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expr = char + ' ' + operand1 + ' ' + operand2
            stack.append(prefix_expr)
    return stack[-1]

## Q7. Write a program to convert prefix expression to infix expression.

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(prefix_expr):
    stack = []
    for char in reversed(prefix_expr.split()):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expr = f"({operand1} {char} {operand2})"
            stack.append(infix_expr)
    return stack[-1]




## Q8. Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_balanced(code_snippet):
    stack = []
    open_brackets = {'(', '[', '{'}
    close_brackets = {')', ']', '}'}
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in code_snippet:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0




## Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty():
        temp_stack.push(stack.pop())

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())




## Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []  # To keep track of the minimum element

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()
            return item

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_minimum(self):
        if not self.is_empty():
            return self.min_stack[-1]


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(7)
    stack.push(1)

    print("Minimum Element:", stack.get_minimum())

