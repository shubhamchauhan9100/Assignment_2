"""
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
#take size of list of tuples
lst_size=int(input("enter list size: "))
lst=[]

#take each element of tuple seperatly
for i in range(lst_size):
    a=int(input(f"enter tuple:{i+1} \nelement1:"))
    b=int(input("element2:"))
    lst.append((a,b))

#sorting based on later element of tuple in list
for i in range(lst_size):
    for j in range(i,lst_size):
        if lst[i][1]>lst[j][1]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)