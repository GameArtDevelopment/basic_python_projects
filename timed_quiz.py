import pyinputplus as pyip
import random
import time
print('')
print('='*13)
print('* Math Quiz *')
print('='*13)
print('')
print('You have 8 seconds between questions!')
print('')


def generate_question():
    """Generate a random math question with addition, subtraction, multiplication, or division"""
    num_1 = random.randint(0, 9)
    num_2 = random.randint(1, 9)

    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        correct_answer = num_1 + num_2
        prompt = f'What is {num_1} + {num_2}? '
    elif operator == '-':
        correct_answer = num_1 - num_2
        prompt = f'What is {num_1} - {num_2}? '
    elif operator == '*':
        correct_answer = num_1 * num_2
        prompt = f'What is {num_1} x {num_2}? '
    elif operator == '/':
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1

        correct_answer = round(num_1 / num_2, 2)
        prompt = f'What is {num_1} / {num_2} (rounded to 2 decimal places)? '

    return prompt, correct_answer


question_range = random.randint(5, 10)
number_of_questions = question_range
correct_answers = 0

for question in range(number_of_questions):

    prompt, correct_answer = generate_question()

    try:
        user_answer = pyip.inputStr(prompt, timeout=8, limit=3)

        if '/' in prompt:
            if abs(float(user_answer) - correct_answer) < 0.01:
                print('Correct!')
                correct_answers += 1
            else:
                print('Incorrect!')
        else:
            if user_answer == str(correct_answer):
                print('Correct!')
                correct_answers += 1
            else:
                print('Incorrect!')
    except pyip.TimeoutException:
        print('Time Over!')
    except pyip.RetryLimitException:
        print('Maybe Next Time!')

    time.sleep(1)

print(f'Score: {correct_answers} / {number_of_questions}')
