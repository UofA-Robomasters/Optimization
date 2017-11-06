import pickle

alpha = 0.5
pkl_file = open("v_table.pkl", 'rb')
v_table = pickle.load(pkl_file)
reward = float(input())
ans2idx = {"A": 0,
           "B": 1,
           "C": 2,
           "D": 3}
while True:
    try:
        input_string = input()
    except EOFError:
        break
    try:
        int(input_string.split()[0][:-1])
    except:
        continue
    input_string = input()
    ans = input_string[0]
    question = input_string[1:]
    question.strip()
    if question in v_table.keys():
        # print(alpha * (reward - v_table[question][ans2idx[ans]]), reward, v_table[question][ans2idx[ans]])
        v_table[question][ans2idx[ans]] = v_table[question][ans2idx[ans]] + alpha * (reward - v_table[question][ans2idx[ans]])
    else:
        v_table[question] = [0, 0, 0, 0]
        v_table[question][ans2idx[ans]] = reward

output = open("v_table.pkl", 'wb')
pickle.dump(v_table, output)
output.close()