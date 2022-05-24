def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        res = args[0]
        for num in args[1:]:
            if num != 0:
                res *= num
            else:
                return 0
        return res
    elif operator == "-":
        res = args[0]
        for num in args[1:]:
            res -= num
        return res
    elif operator == "/":
        res = args[0]
        for num in args[1:]:
            if num != 0:
                res /= num
            else:
                return 0
        return res


print(operate("-", 2, 2, 2))
print(operate("-", 3, 0, 5))
