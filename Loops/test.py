# # A=[10,20,30,40,50]
# # f=[3,5,2,7,9]

# # # total of the product of the f and A using loop
# # total_Af=0
# # for i in range(len(A)):
# #     num=A[i]*f[i]
# #     total_Af+=num
# # print(total_Af)

# # #total sum of frequency using loop
# # total_f=0
# # for i in f:
# #     total_f+=i

# # #calculating the mean
# # print(f"Mean Value: {total_Af/total_f}")


# data=[(10,20),(20,30),(30,40),(40,50)]
# frequency=[5,8,6,7]

# #calculating the mid points using the loop
# mid_points=[]
# for i in data:
#     mid_points.append((i[0]+i[1])/2)


# # total sum of the multiplication of midpoints and frequency using loop
# total_mf=0
# for i in range(len(mid_points)):
#     mf=mid_points[i]*frequency[i]
#     total_mf+=mf

# total_f=0
# for i in frequency:
#     total_f+=i

# print(f"Mean Value: {total_mf/total_f}")




# def calculate_mean(data,frequency):
#     # calculating the list of the mid points
#     mid_points = []

#     for i in data:
#         mid_points.append((i[0]+i[1])/2)

#     # calculating total sum of (m×f)
#     total_mf = 0

#     for i in range(len(mid_points)):
#         mf = mid_points[i] * frequency[i]
#         total_mf += mf

#     # calculating total sum of frequencies
#     total_f = 0

#     for i in frequency:
#         total_f+= i

#     # calculating mean
#     mean = total_mf/total_f

#     return mean


# def find_mean(data):
#     total = sum(data)
#     n = len(data)
#     mean = total / n
#     return mean


# B = [40, 50, 60, 70, 80, 90]
# C = [98, 67, 45, 23]

# print(range(len(B),len(C)))

A= "bakchodi"
while A=="bakchodi":
    print("Group Locked")