from collections import defaultdict

int_dict = defaultdict(int)
int_dict['a'] += 1
print(int_dict)

print(int_dict.get('a'))