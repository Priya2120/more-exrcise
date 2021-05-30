Alphabate =input("enter the number :")
Charater=input("enter the charater :")
num=int(input("enter the  number :"))
if Alphabate>"a"and Alphabate<="z" or Alphabate>="a" and Alphabate<"z":
    print(Alphabate)
    if Charater=="@" or Charater=="#" or Charater=="$" or Charater=="&":
        print(Charater)
        if num>=0:
            print(Alphabate+Charater+str(num))
        else:
            print ("incorrect number ")
    else:
        print("incorrect charater")
else:
    print("incorrect alphabate")
