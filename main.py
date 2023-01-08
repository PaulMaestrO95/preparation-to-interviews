class Stack():
    def __init__(self):
        self.main_stack = []

    def is_empty(self):
        if self.main_stack == []:
            return True
        else:
            return False

    def push(self, new_element):
        self.main_stack.insert(0, new_element)
        pass

    def pop(self):
        if self.is_empty() is False:
            return self.main_stack.pop(0)
        else:
            return False

    def peek(self):
        if self.is_empty() is False:
            return self.main_stack[0]
        else:
            return False

    def size(self):
        return len(self.main_stack)


def check(str) -> str:

    braces = Stack()
    parenthesis = Stack()
    square_brackets = Stack()
    true = 'Сбалансированно'
    false = 'Несбалансированно'

    my_list = list(str)

    for sign in my_list:
        if sign == '(':
            parenthesis.push(sign)
        elif sign == ')':
            if parenthesis.peek() is False:
                return false
            else:
                parenthesis.pop()

        elif sign == '[':
            square_brackets.push(sign)
        elif sign == ']':
            if square_brackets.peek() is False:
                return false
            else:
                square_brackets.pop()

        elif sign == '{':
            braces.push(sign)
        elif sign == '}':
            if braces.peek() is False:
                return false
            else:
                braces.pop()

    if parenthesis.size() == 0 and square_brackets.size() == 0 and braces.size() == 0:
        return true
    else:
        return false


if __name__ == '__main__':
    print(check('(((([{}]))))'))  # сбалансировано
    print(check('[([])((([[[]]])))]{()}'))  # сбалансировано
    print(check('{{[()]}}'))  # сбалансировано
    print(check('}{}'))  # несбалансировано
    print(check('{{[(])]}}'))  # несбалансировано
    print(check('[[{())}]'))  # несбалансировано
