##List adder
a = input()
list_a = list(map(int, a.split()))
print (list_a)

b = input()
list_b = list(map(int, b.split()))
print (list_b)

new_list=[]
new_list.append(list_a[0]+list_b[1])
new_list.append(list_a[2]+list_b[3])
print (new_list)
