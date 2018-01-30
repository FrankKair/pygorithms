#!/usr/bin/env python3
import os
from subprocess import check_output


def print_all_euler_results():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    for filename in os.listdir(dir_path):
        if filename.endswith(".py") and filename.startswith("0"):            
            command = "python3 {file}".format(file=filename)

            output = str(check_output(command, shell=True))
            l = [int(x) for x in output if x in ['0','1','2','3','4','5','6','7','8','9']]
            result = ''.join(map(str, l))

            problem_number = filename.replace('.py', '')

            out = ("Problem {number}: {result}").format(
                number=problem_number,
                result=result
            )

            print(out)


print_all_euler_results()
