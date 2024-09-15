Time of the Year 
Given the number of seconds elapsed since the epoch [01-01-1970 00:00:00 Thursday], you need to find the current date, along with the day.



Note: Do not use any inbuilt functions / libraries for your main logic.

Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains the number of seconds elapsed since the epoch.



Output Format

For each test case, print the date in DD-MMM-YYYY format, followed by the day, separated by a new line.



Constraints

1 <= T <= 10000

0 <= S <= 109



Example

Input

10

86399

86400

2592000

2678400

8639999

8640000

31535999

31536000

68169599

68169600



Output

01-JAN-1970 Thursday

02-JAN-1970 Friday

31-JAN-1970 Saturday

01-FEB-1970 Sunday

10-APR-1970 Friday

11-APR-1970 Saturday

31-DEC-1970 Thursday

01-JAN-1971 Friday

28-FEB-1972 Monday

29-FEB-1972 Tuesday



Explanation



Self Explanatory





# Enter your code here. Read input from
def find(sec):
    daysinmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    monthnames=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    daynames=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    year,month,date,day=1970,0,1,3
    sec_in_day=24*60*60
    da=sec//sec_in_day
    while da>=365:
        if (year%4==0 and year%100!=0) or(year%400==0):
            if da>=366:
                da-=366
                year+=1
            else:
                break
        else:
            da-=365
            year+=1
    if (year%4==0 and year%100!=0) or(year%400==0):
        daysinmonth[1]=29
    for i in range(12):
        if da<daysinmonth[i]:
            month=i
            date=da+1
            break
        else:
            da-=daysinmonth[i]
    day=(3+sec//sec_in_day)%7
    if date<10:
        print('0%d'%date,end="")
    else:
        print(date,end="")
    print("-%s"%monthnames[month],end="")
    print("-%s"%year,end="")
    print(" %s"%daynames[day],end="")
    print()

for _ in range(int(input())):
    sec=int(input())
    find(sec)