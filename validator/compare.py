import timeit

import loginvalidate

logins_fp = 'logins.txt'
logins_number = 10**6
compare_result_fp = 'compare.txt'
repeat_number = 10

code_template = '''
with open(logins_fp, 'r', encoding='utf-8') as file:
    for line in file:
        {validate}(line)
'''


def get_elapsed_time(function):
    func_name = function.__name__

    return timeit.timeit(
        code_template.format(validate=func_name),
        number=repeat_number,
        globals={
            'logins_fp': logins_fp,
            func_name: function
        }
    ) / repeat_number


def main():
    with open(compare_result_fp, 'w', encoding='utf-8') as file:
        for func in (
                loginvalidate.is_login_valid_regex,
                loginvalidate.is_login_valid_python_lambdas,
                loginvalidate.is_login_valid_python
        ):
            t = get_elapsed_time(func)/logins_number
            result = f'* {round(t, 10)} s\t-\t{func.__name__}\n'
            file.write(result)
            print(result)


if __name__ == '__main__':
    main()
