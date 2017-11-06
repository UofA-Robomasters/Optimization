import pickle
pkl_file = open("v_table.pkl", 'rb')
v_table = pickle.load(pkl_file)
question = input()
question.replace(" ", "")
print(v_table[question])