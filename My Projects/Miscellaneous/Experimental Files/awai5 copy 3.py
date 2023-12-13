our_str = 'anant upadhyay'

def solve():
    s2=[]
    s1 = our_str.split(sep=' ')
    for word in s1:
        word = word.capitalize()
        s2.append(word)
    s1 = s2
    # print(s1)
    print(*s1)

solve()
