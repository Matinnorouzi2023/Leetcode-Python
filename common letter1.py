" INTERVIEW QUESTION - Find out common letters between two strings Using Python"

def common_letters():
    str1 =input("Enter first string:")
    str2 =input("Enter first string:")
    s1=set(str1)
    s2=set(str2)
    cletter=s1 & s2
    print(cletter)
    
common_letters()