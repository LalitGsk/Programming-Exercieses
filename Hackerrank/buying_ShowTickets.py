'''Buying Show Tickets
A function that returns the wait time in Queue to buy total n tickets where each transaction takes one unit of time.
Input e.g - [1,2,5]
'''

def waitingTime(tickets, p):
    total_steps = tickets[p]
    first_half = tickets[:p]
    second_half = tickets[p+1:]

    for num in first_half:
        if num < tickets[p]:
            total_steps += num
        else:
            total_steps += tickets[p]

    for num in second_half:
        if num < tickets[p]:
            total_steps += num
        else:
            total_steps += tickets[p] - 1

    return total_steps
