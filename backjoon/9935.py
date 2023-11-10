if __name__ == "__main__":
    string_value = input()
    trigger_keyword = input()
    stack = []
    # while string_value.find(trigger_keyword) != -1:
    #     string_value = string_value.replace(trigger_keyword,"")

    # if len(string_value) == 0:
    #     print("FRULA")
    # else:
    #     print(string_value)
    len_value = len(trigger_keyword)

    for i in string_value:
        stack.append(i)
        if "".join(stack[-len_value:]) == trigger_keyword:
            for _ in range(len_value):
                stack.pop()

    if len(stack) == 0:
        print("FRULA")
    else:
        print("".join(stack))
