import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# print(data)
# print(pd.get_dummies(data['whoAmI']))

robot_lst = []
human_lst = []
for i in range(len(lst)):
    if lst[i] == 'robot':
        robot_lst.append(True)
        human_lst.append(False)
    if lst[i] == 'human':
        robot_lst.append(False)
        human_lst.append(True)
data1 = pd.DataFrame({'human': human_lst, 'robot': robot_lst})
print(data1)