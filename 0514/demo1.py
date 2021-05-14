#直到使用者輸入對的
flag = True 
while flag:
    try:
        x=int(input("number:"))
    except ValueError:
        print("Error!!")
    else:
        print(x)
        flag = False