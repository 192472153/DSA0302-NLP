# DFA for strings ending with "ab"

transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

current_state = 'q0'
final_state = 'q2'

string = input("Enter String: ")

path = [current_state]

valid = True

for ch in string:
    if ch not in ['a', 'b']:
        valid = False
        break
    current_state = transitions[current_state][ch]
    path.append(current_state)

print("Transition Path:")
print(" -> ".join(path))

if valid and current_state == final_state:
    print("Accepted")
else:
    print("Rejected")
