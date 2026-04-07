from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

def main():
    postfix_expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]
    
    print("----- Postfix Evaluator -----")
    evaluator = PostfixEvaluator()
    
    for expr in postfix_expressions:
        result = evaluator.evaluate(expr)
        print(f"[{expr}] = {result}")

    print("\n----- Infix to Postfix Converter -----")
    infix_expressions = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A +  ( B - C ) * D",
        "( A + B * ( C - D ) ) / E"
    ]
    
    converter = InfixToPostfixConverter()
    
    for expr in infix_expressions:
        result = converter.convert(expr)
        print(f"[{expr}] -> [{result}]")

if __name__ == "__main__":
    main()