#  Simulate a loop that ends only when 'quit' is received. (Test logic only, no actual input)

def simulate_input_loop(inputs):
    i = 0
    result = []
    while i < len(inputs) and inputs[i] != 'quit':
        result.append(inputs[i])
        i += 1
    return result

assert simulate_input_loop(['hello', 'world', 'quit', 'ignored']) == ['hello', 'world']

