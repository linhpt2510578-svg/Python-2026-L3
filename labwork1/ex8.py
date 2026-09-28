l = [1,4,5,6,7,8]

def extract_even(l):
    return [x for x in l if x % 2 == 0]
print(extract_even(l))