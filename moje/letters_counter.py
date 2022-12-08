text = "kajak"
# uniqe_text = ''.join(set(text))
# print(uniqe_text)
#
# text = "aaaabbbbccccddddd"
# print(set(text))
#
# uniqe_text = ''.join(set(text))
# print(uniqe_text)
#
# result = {}
# for i in text:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
#
# print(result)

#solution 1
unique_letters = []
for letter in text:
    if letter not in unique_letters:
        unique_letters.append(letter)
print(unique_letters)

letters_dict = {}
for letter in unique_letters:
    letters_dict[letter] = text.count(letter)
print(letters_dict)


#solution 2
letters_dict = {}
for letter in text:
    if letter not in letters_dict:
        letters_dict[letter] = 1
    else:
        letter
print(letters_dict)
#nie sko nczone