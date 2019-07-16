while True:
    import shutil
    n = int(input("数："))
    if n == 0:
        break
    pic = ["_"+str(i)+".jpg" for i in range(1,n+1)]
    pathf = [input("{}：".format(i)) for i in range(1,n+1)]
    s = int(input("はじまり："))
    e = int(input("おわり："))
    for i in range(s,e+1):
        for j in range(n):
            shutil.copy(pathf[j],str(i)+pic[j])
    print("c")