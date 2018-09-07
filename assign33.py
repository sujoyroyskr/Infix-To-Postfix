class Assign33:

    def infixconversiontopostfix(self, equation):

        for i in equation:

            if self.isOperand(i):
                self.operand.append(i)
            else:
                self.operator.append(i)

           
        for i in self.operand:
            self.output.append(i)
        for i in reversed(self.operator):
            self.output.append(i)
        print "".join(self.output)


    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.operator = []
        self.operand = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]
    #peek function returns the value of the top of the stack

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False


equation = "a+b-c*d/(e^f)^g"
obj = Assign33(len(equation))
obj.infixconversiontopostfix(equation)