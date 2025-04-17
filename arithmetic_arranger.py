'''
This function will take in a list of arithmetic problems and arrange them vertically like you do in primary school. Objective is to improve readibility. 

The arithmetic_arranger will take in a list of problems and has a optional True or False value for show_answers. If it is true it will append the answers to the output. 

It will return error messages for the following scenarios:
	1. more than 5 problems. The reasonning behind this is it will cause wrap issues in the output. 
	2. operands must be + or -. 
	3. The problems must only contain digits. 
	4. The numbers cannot be more than 4 digits.

'''


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

	#making empty lists that will store the formatted values
    top_level = []
    bottom_level = []
    dash_line = []
    answers = []
	
	
    for problem in problems:
    	#we need to split the equations based on their operands
        if '+' in problem:
            parts = problem.split('+')
            operator = '+'
        elif '-' in problem:
            parts = problem.split('-')
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."
		
		#removing leading or trailing zeros
        first = parts[0].strip() 
        second = parts[1].strip()
		
		#both values must only contain digits
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
		
		#both values can only be a max length of 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
		
		#we will need to add leading spaces so that both valeus have the same length
		# add 2 for an additional space and the operand in the second line
        width = max(len(first), len(second)) + 2
        top_level.append(first.rjust(width))
        bottom_level.append(operator + second.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(first) + int(second))
            else:
                answer = str(int(first) - int(second))
            answers.append(answer.rjust(width))

    # Combine lines with 4 spaces between each problem
    # using a multi line string to make this compact
    arranged_problems = (
        '    '.join(top_level) + '\n' +
        '    '.join(bottom_level) + '\n' +
        '    '.join(dash_line)
    )
	#append the answers
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems


# Example usage
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
