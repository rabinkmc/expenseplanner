from collections import deque, OrderedDict

input = {'budget': 10000, 'saving':3000 } 
priorities = [ ('rent', 3000),
              ('food', 200), 
              ('hook',300),
              ('battery', 999) ] 
 
can_buy = [ ] 
available_budget = input['budget'] - input['saving']

status = 0; 
# 1 if priorities are not met

for priority in priorities:
    
    if priority[1] < available_budget:
        can_buy.append(priority)
        available_budget -= priority[1]

    else:
        status = 1



    

