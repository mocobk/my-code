mylist = ["11","2","a","4"]
for i in mylist:
    try:
        num = int(i)
    except ValueError as reason:
        print("出错了，原因是："+ str(reason))
    # finally:
    print(str(num)+"end")
