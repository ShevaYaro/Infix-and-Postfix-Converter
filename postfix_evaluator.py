from stack import Stack

class PostfixEvaluator:
    def evaluate(self, expression):
        """Evaluates a postfix expression and returns the result."""
        stack = Stack()
        
        tokens = expression.split()

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                if token == '+':
                    result = left_operand + right_operand
                elif token == '-':
                    result = left_operand - right_operand
                elif token == '*':
                    result = left_operand * right_operand
                elif token == '/':
                    result = left_operand / right_operand
                
                stack.push(result)
            
            else:
                stack.push(int(token))
                
        return stack.pop()