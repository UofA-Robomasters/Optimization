# for50%!

### Usage
Training
1. save quizzes into text files like 'first.txt', 'second.txt'
2. run scripts in such order.
```commandline
python3 first_time.py < first.txt
python3 more_time.py < second.txt
python3 more_time.py < third.txt
```
and so for other text files.

Prediction
3. save new quiz into text files like 'five_no_ans.txt'
4. predict all answers
```commandline
python3 greedy_all.py < five_no_ans.txt
```
5. predict one answer
```commandline
python3 greedy_one.py
```
copy and paste the question of which you wish to know the values.