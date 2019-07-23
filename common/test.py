test_list = ["()", "()[]{}", "(]", "([)]", "{[]}", "]", "[", "[([]])", "(])"]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.isValid(test_value))
assert answers == [True, True, False, False, True, False, False, False, False], str(answers) + ' is wrong solution'
print('Everything looks fine!')


def check_solution(func, test_data, real_data):
    answers = []
    for test_value in test_data:
        answers.append(func(test_value))