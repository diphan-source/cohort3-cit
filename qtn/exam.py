"""
THEY SAY that grass is always greener on the other side . 
this means that other people always seem to be doing better than you 
since we are programmers , we can quantify the greenness of all the other sides by writing some code 

there are n gardens in a row . the gardens are numbered 1 to n and the i-th garden has a greenness
of a[i]. with higher numbers representing greener gardens . lets us define the greenness on 
the other side for owner of the i-th garden as the greenest garden besides the i-th garden 

Create a program to enumerate all of the "greenness on the other side" for every garden in a row 

give the greenness of n gardens , please calculate the "greeness on the other side" for each garden 



"""

def greenness_on_the_other_side(gardens):
    n = len(gardens)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            if gardens[i] < gardens[j]:
                result[i] = max(result[i], gardens[j])
    return result

if __name__ == "__main__":
    gardens = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    print(greenness_on_the_other_side(gardens))