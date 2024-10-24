import sys 

file_name = sys.argv[1]
file = open(file_name, 'r') 
list = file.readlines()

def singleton(lst, start, end):
    if start == end:
        print(lst[start])
        return None
    
    mid = (start + end) // 2
    
    #even indexes are the first occurence of a duplicate so if not, call function on the left side
    #odd indexes are the second occurence of a duplicate so if not, call function on the left side
    if (mid % 2 == 0 and lst[mid] == lst[mid + 1]) or (mid % 2 == 1 and lst[mid] == lst[mid - 1]):
        singleton(lst, mid + 1, end)
    else:
        singleton(lst, start, mid)

singleton(list, 0, len(list)-1)


"""def singleton(list, start, end):
  
    if start == end:
        print(list[start])
        return None 
   
    mid = (start + end) // 2


        #if odd and its left is equal then call to right side
    if mid % 2 == 1 and list[mid] == list[mid - 1]:
            singleton(list, mid + 1, end)
    elif mid % 2 == 1 and list[mid] == list[mid + 1]:
        singleton(list, start, mid - 1)
    elif mid % 2 == 0 and list[mid] == list[mid - 1]:
         singleton(list, start, mid-1)
    elif mid % 2 == 0 and list[mid] == list[mid + 1]:
         singleton(list, mid + 1, end)
    else: 
        print (list[mid])

singleton(list, 0, len(list)-1)"""


