# python3
import sys
def read_input():
    inp = input().rstrip()
    if inp == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif inp == 'F':
        filename = input()
        with open("tests/" + filename, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p_len, t_len = len(pattern), len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    output = []
    for i in range(t_len - p_len + 1):
        if t_hash == p_hash and text[i:i+p_len] == pattern:
            output.append(i)
        if i + p_len < t_len:
            t_hash = hash(text[i+1:i+p_len+1])
    return output


# this part launches the functions
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = '06'
    print_occurrences(get_occurrences(*read_input()))

