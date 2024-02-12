from argparse import ArgumentParser
import sys



def evaluate(expression):
    """
    Evaluates a postfix expression.
    
    Args:
        expression (str): A string containing a postfix expression, with elements separated by spaces.
    
    Returns:
        float: The result of the postfix expression.

    """
    operand_stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operators:
            operand_stack.append(float(token))
        else:
            # if token is an operator, pop two operands and apply the operator
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-': 
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/': 
                result = operand1 / operand2
            
            operand_stack.append(result)  
            
    return operand_stack[0]  
    
def main(file_path):
    """
    Read a file of postfix expressions, evaluate each expression, and print the results.
    
    Args:
        file_path (str): A string containing the path to a file of postfix expressions.
    
    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other unexpected errors.
        
    Returns:
        Nothing
    
    Side effects:
        Prints the evaluated results for each expression.
    

    """
    try:
        with open(file_path, 'r') as fname:
            for line in fname:
                result = evaluate(line)
                print(f"{line.strip()} = {result}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")



def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
