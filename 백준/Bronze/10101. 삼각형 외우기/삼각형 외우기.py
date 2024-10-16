angle_list=[int(input()) for i in range(3)]
if sum(angle_list)!=180:
    print("Error")
elif angle_list[0]==angle_list[1]:
    if angle_list[0]==angle_list[2]:
        print("Equilateral")
    else:
        print("Isosceles")
elif angle_list[1]==angle_list[2]:
    print("Isosceles")
elif angle_list[0]==angle_list[2]:
    print("Isosceles")
else:
    print("Scalene")