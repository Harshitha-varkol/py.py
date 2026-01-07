# l=[3,4,5,67,89,43,56]
# target=89
# for i in range(len(l)+1):
#     if l[i]==target:
#         print("the targeted number is",l[i])
#         break
# else:
#     print("the number not found")    



# l=[4,5,3,5,6,4,3,5,]
# target=5
# for i in range(len(l)):
#     if l[i]==target:
#         print("the targeted element is",l[i])
#         break
# else:
#     print("the element is not found")    



# l=[4,5,3,5,6,4,3,5,77,34,89,32]
# target=8
# for i in range(len(l)):
#     if l[i]==target:
#         print("the targeted element is",l[i])
#         break
# else:
#     print("the element is not found")        


# l=[4,5,3,5,6,4,3,5,77,34,89,32]
# target=77
# for i in range(len(l)):
#     if l[i]==target:
#         print("the targeted element is",l[i])
#         break
# else:
#     print("the element is not found")            


# l=[4,5,3,5,6,4,3,5,77,34,89,32]
# target=8
# for i in range(len(l)):
#     if l[i]==target:
#         print("the targeted element is",l[i])
#         break
# else:
#     print("the element is not found")            

# arr=[1,2,3,4,5,6,7,8,9,10,77,98,44,87]
# low=0
# high=len(arr)-1
# # print(high)
# target=98
# while low<=high:
#     mid=(low+high)//2
#     if target==arr[mid]:
#         print("the targeted element is",arr[mid])
#         break
#     elif target>arr[mid]:
#         low=mid+1
#     else:
#         high=mid-1    

       
# arr=[3,1,6,9,3,7,90,33,89,32,87,88,10]
# for i in range(len(arr)):
#     min=i
#     for j in range(i+1,len(arr)):
#         if arr[min]>arr[j]:
#             min=j
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)  
#   
# low=0
# high=len(arr)-1
# target=98
# while low<=high:
#     mid=(low+high)//2
#     if target==arr[mid]:
#         print("the targeted element is",arr[mid])
#         break
#     elif target>arr[mid]:
#         low=mid+1
#     else:
#         high=mid-1    

   


# arr=[3,4,3,9,1,0,3,89,4,6,4]
# for i in range(len(arr)):
#     min=i
#     for j in range(i+1,len(arr)):
#         if arr[min]>arr[j]:
#             min=j
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)           

# arr=[3,1,6,9,3,7,90,33,89,32,87,88,10]
# for i in range(len(arr)):
#     min=i
#     for j in range(i+1,len(arr)):
#         if arr[min]>arr[j]:
#             min=j
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)  
      

lst=[1,3,9,24,4,3,2,9,4,3,9,5,44,3,2,90,100]
minimum=lst[0]
maximum=lst[0]
for i in range(len(lst)):
    if i>minimum:
        minimum=i
    else:
        maximum=i
print(maximum)
print(minimum)        





            