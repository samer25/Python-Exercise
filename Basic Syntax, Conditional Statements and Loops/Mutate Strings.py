# You will be given two strings. Transform the first string into the second one, one letter at a time and print it.
# Print only the unique strings Note: the strings will have the same lengths

f_string = str(input())
s_string = str(input())
f_list = [x for x in f_string]
for i in range(len(s_string)):
    if f_string[i] != s_string[i]:
        f_list[i] = s_string[i]
        print(''.join(f_list))
