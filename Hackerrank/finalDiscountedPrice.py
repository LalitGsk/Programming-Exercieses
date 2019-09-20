'''Function returning the final Discounted price where
1. each item discounted at its fullPrice-price(first lower/equal priced item to its right.) 
2. else item sold at its fullPrice.
Input e.g - [2,3,1,2,4,2]
'''

def finalPrice(prices):
    # Write your code here
    discounted_p=[]
    for i in range(len(prices)):
        piv=prices[i]
        for j in range(i+1,len(prices)-1):
            if(prices[piv]>=prices[j]):
                discounted_p.append(prices[piv]-prices[j])
                break
            elif prices[piv]<prices[j]:
                continue
            else:
                discounted_p.append(prices[piv])

    print(sum(discounted_p))
    for m in range(len(prices)):
        if(prices[m]==discounted_p[m]):
            print(m)
