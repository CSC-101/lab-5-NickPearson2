import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: data.Time, time2: data.Time)->data.Time:
    total_time = data.Time(0,0,0)
    total_time.second += time1.second + time2.second
    if(total_time.second >= 60):
        total_time.minute += 1
        total_time.second -= 60
    else:
        total_time.second = (time1.second + time2.second)
    total_time.minute += time1.minute + time2.minute
    if ( total_time.minute >= 60):
        total_time.hour += 1
        total_time.minute -= 60
    else:
        total_time.minute = (time1.minute + time2.minute)
    total_time.hour += (time1.hour + time2.hour)
    return total_time
# Part 4
def is_descending(list:list[float])->bool:

    for i in range(len(list)-1):
        if(list[i] <= list[i+1]):
            return False
    return True

# Part 5
def largest_between(the_list:list[int],lower,upper)->int:
    if(lower>upper):
        return None
    #If upper more than index of last element, subtract difference between upper and index of last element, equal it to upper
    if(upper > (len(the_list)-1)):
        sub = upper-(len(the_list)-1)
        upper-=sub
    #If lower less than 0, set it to 0 to avoid indexOutOfBounds error
    if(lower < 0):
        lower = 0
    max = the_list[lower]
    idx = 0
    for i in range(lower,upper+1):
        if(the_list[i]>max):
            max = the_list[i]
            idx = i
    return idx


# Part 6
def furthest_from_origin(list:[data.Point]) -> data.Point:
    if(list == []):
        return None
    point = list[0]
    for i in range(len(list)-1):
        diff_x = list[i+1].x-list[i].x
        diff_y = list[i+1].y-list[i].y
        if(diff_x>0 and diff_y>=0):
            point = list[i+1]
        elif(diff_x<=0 and diff_y>0):
            point = list[i]
    return point