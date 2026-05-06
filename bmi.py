def calculate_bmi(weight,height):
    print ("Height = "+ str(height))
    print ("weight = "+ str(weight)) 

    bmi = weight / (height*height)
    print (bmi)

    if bmi < 18.5:
        return -1
    elif bmi < 25:
        return 0
    elif bmi > 25:
        return 1


print(calculate_bmi(1000,1.67))
