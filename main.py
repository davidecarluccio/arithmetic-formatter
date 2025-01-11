def arithmetic_arranger(problems, show_answers=False):
    # Error checks
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and one operator."

        num1, operator, num2 = parts

        # Validate operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Validate numbers
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Validate number length
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate result if needed
        result = ""
        if show_answers:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))

        # Format lines
        width = max(len(num1), len(num2)) + 2
        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dashes.append("-" * width)
        if show_answers:
            results.append(result.rjust(width))

    # Combine lines
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes)
    )
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)
    
    return arranged_problems
