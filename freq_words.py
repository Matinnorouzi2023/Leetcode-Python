"INTERVIEW QUESTION - Count the frequency of words appearing in a string Using Python"


def freq_words():
    str=input("please enter your string:")
    li=str.split(" ")       
    d={}
    for i in li:
       if i not in d.keys():
          d[i]=0
       d[i] = d[i] + 1
    print(d)

freq_words()

"i love apple and my mother love apple too."