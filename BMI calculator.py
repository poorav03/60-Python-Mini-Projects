from scipy.stats import bayes_mvs

height = float(input("Enter the height: "))
weight = float(input("Enter the weight: "))
height = height/100
BMI = weight/(height*height)
print("Your BMI is ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are under weight")
    elif(BMI<=18.5):
        print("You are fit")
    elif(BMI<=22.5):
        print("You are healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are seriously overweight")
else:
    print("Enter valid details")
