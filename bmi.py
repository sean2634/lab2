def calculate_bmi(weight,height):
    print ("Height = "+ str(height))
    print ("weight = "+ str(weight)) 

    bmi = weight / (height*height)
    print (bmi)

    if bmi < 18.5:
        print ("underweight")
    elif bmi < 25:
        print ("normal weight")
    elif bmi > 25:
        print ("over mouth")


calculate_bmi(weight=67, height=1.67)
