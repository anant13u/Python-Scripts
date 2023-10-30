import re

phrase = 'My name is Anant Upadhyay. I was born on 9th October, 1989.'

our_match = re.search(r'\d{4}', phrase)
our_match_2 = re.search(r'\d', phrase)

print(our_match.group())
# 1989

print(our_match.span())
# (54, 58)

print(our_match_2.group())
# 9
