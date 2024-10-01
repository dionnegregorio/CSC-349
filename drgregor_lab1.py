import sys 

file_name = sys.argv[1]
file = open(file_name, 'r') 
list = file.readlines()

"""def singleton(list, start, end):
  
    if start == end:
        print(list[start])
        return None 
   
    mid = (start + end) // 2

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

def singleton(lst, start, end):
    if start == end:
        print(lst[start])
        return None
    
    mid = (start + end) // 2
    
    if (mid % 2 == 0 and lst[mid] == lst[mid + 1]) or (mid % 2 == 1 and lst[mid] == lst[mid - 1]):
        singleton(lst, mid + 1, end)
    else:
        singleton(lst, start, mid)

singleton(list, 0, len(list)-1)
