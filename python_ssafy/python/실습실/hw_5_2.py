# 아래 함수를 수정하시오.
def count_character(input_word, find_word):
    return input_word.count(find_word)


result = count_character("Hello, World!", "o")
print(result)  # 2
