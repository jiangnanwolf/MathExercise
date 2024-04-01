import random
from datetime import datetime

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


class MathExercise:
    def __init__(self, n: int, maxNumber: int):
        self.n = n
        self.maxNumber = maxNumber


    def sub(self):
        operations = ['+', '-', '×', '÷']
        operation = random.choice(operations)
        num1, num2, result = -1, -1, -1
        if operation == '-':
            num2 = random.randint(1, self.maxNumber - 1)
            num1 = random.randint(num2, self.maxNumber)
            result = num1 - num2
        elif operation == '÷':
            num2 = random.randint(1, self.maxNumber//3)
            num1 = num2 * random.randint(1, self.maxNumber//num2)
            result = num1 // num2
        elif operation == '×':
            num1 = random.randint(0, self.maxNumber//3)
            num2 = random.randint(0, self.maxNumber//3)
            result = num1 * num2
        else:
            num1 = random.randint(1, self.maxNumber)
            num2 = random.randint(1, self.maxNumber)
            result = num1 + num2
        return (num1, operation, num2, result)


    def sub_at_left(self):
        operations = ['+', '-', '×', '÷']
        operation = random.choice(operations)
        num, result, upper = -1, -1, 5
        sub = self.sub()
        if operation == '+':
            num = random.randint(0, self.maxNumber)
            result = num + sub[3]
        elif operation == '-':
            num = random.randint(0, sub[3])
            result = sub[3] - num
        elif operation == '×':
            if sub[3] != 0:
                upper = self.maxNumber // sub[3] + 1
            num = random.randint(0, upper)
            result = num * sub[3]
        else:
            divs = find_divisors(sub[3])
            if divs:
                num = random.choice(divs)
            else:
                num = random.randint(1, sub[3] + 2)
            result = sub[3] // num
        
        if (sub[1] == '+' or sub[1] == '-') and (operation == '×' or operation == '÷'):
            return ('(', sub[0], sub[1], sub[2], ')', operation, num, result)
        else:
            return (sub[0], sub[1], sub[2], operation, num, result)
            

    def sub_at_right(self):
        operations = ['+', '-', '×', '÷']
        operation = random.choice(operations)
        num, upper = -1, 5
        sub = self.sub()
        if operation == '+':
            num = random.randint(0, self.maxNumber)
            result = num + sub[3]
        elif operation == '-':
            num = random.randint(sub[3], sub[3] + self.maxNumber)
            result = num - sub[3]
        elif operation == '×':
            if sub[3] != 0:
                upper = self.maxNumber // sub[3]
            num = random.randint(0, upper)
            result = num * sub[3]
        else:
            result = random.randint(1, self.maxNumber//3)
            num = sub[3] * result
        
        if ((sub[1] == '×' or sub[1] == '÷') and (operation == '+' or operation == '-')) or (sub[1] == '+' and operation == '+') or (sub[1] == '×' and operation == '×'):
            return (num, operation, sub[0], sub[1], sub[2], result)
        else:
            return (num, operation, '(', sub[0], sub[1], sub[2], ')', result)
        

    def generate(self):
        exercises = []
        for i in range(self.n):
            if i % 2 == 0:
                exercises.append(self.sub_at_left())
            else:
                exercises.append(self.sub_at_right())
        return exercises


    def print(self, l, answers=False):
        html = """
        <html>
        <head>
            <style>
                table {
                    width: 100%;
                }
                tr {
                    line-height: 2em;  /* Adjust this value to change the line spacing */
                }
                td {
                    text-align: left;
                }
            </style>
        </head>
        <body>
            <table>
        """
        for i in range(0, len(l), 3):
            html += "<tr>"
            for j in range(3):
                if i + j < len(l):
                    exercise = l[i + j]
                    if len(exercise) == 6:
                        if answers:
                            html += "<td>{}. {} {} {} {} {} = {} </td>".format(i + j + 1, *exercise)
                        else:
                            html += "<td>{}. {} {} {} {} {} = </td>".format(i + j + 1, *exercise)
                    else:
                        if answers:
                            html += "<td>{}. {} {} {} {} {} {} {} = {} </td>".format(i + j + 1, *exercise)
                        else:
                            html += "<td>{}. {} {} {} {} {} {} {} = </td>".format(i + j + 1, *exercise)
            html += "</tr>"
        html += "</table></body></html>"
        return html
    

    def writeMathExercise(self):
        l = self.generate()
        html = self.print(l)
        html_answer = self.print(l, True)

        # Get current date and time
        now = datetime.now()

        # Format as a string
        timestamp_str = now.strftime("%Y%m%d_%H%M%S")

        # Use in filename
        filename = f"{timestamp_str}.html"
        filename_answer = f"{timestamp_str}_answer.html"

        with open(filename, "w") as f:
            f.write(html)
        with open(filename_answer, "w") as f:
            f.write(html_answer)


def main():
    MathExercise(81, 200).writeMathExercise()


if __name__ == "__main__":
    main()
