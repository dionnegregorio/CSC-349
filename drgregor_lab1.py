import sys 

list_input = sys.argv[1]

file = open(list_input, 'r') 

list = file.readlines()

start = 0
end = len(list)

def find_singleton(list):

    start = 0
    end = len(list) - 1

    while start < end:
        middle = (start + end) // 2

        #check if index is odd
        if middle % 2 == 1:
            middle -= 1

        #compare middle num to its right side
        if list[middle] == list[middle + 1]:
            start = middle + 2
        else: 
            end = middle       

    return list[middle + 2];
    
print(find_singleton(list))
