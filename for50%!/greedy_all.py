import pickle

alpha = 0.5
pkl_file = open("v_table.pkl", 'rb')
v_table = pickle.load(pkl_file)
ans2idx = {"A": 0,
           "B": 1,
           "C": 2,
           "D": 3}
idx2ans = {0: "A",
           1: "B",
           2: "C",
           3: "D"}
while True:
    try:
        input_string = input()
    except EOFError:
        break
    try:
        num = int(input_string.split()[0][:-1])
    except:
        continue
    input_string = input()
    question = input_string
    question.strip()
    if question in v_table.keys():
        greedy_ans = idx2ans[v_table[question].index(max(v_table[question]))]
        print(num, ": ", v_table[question], "greedy answer: ", greedy_ans)
    else:
        print(num, ": ", "never encountered.")