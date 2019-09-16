'''
Write a function that returns the min length of a roof covering K cars
'''

def carParkingRoof(cars, k):
    # Write your code here
    cars = sorted(cars)
    roof_len=[]
    left=0
    right=k-1
    while(right<len(cars)):
        roof_len.append(cars[right]-cars[left]+1)
        left+=1
        right+=1

    return min(roof_len)
