# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:39:01 2019

@author: lalit
929:
Given a list of emails, we send one email to each address in the list. 
How many different addresses actually receive mails? 
"""

def numUniqueEmails(emails):
        hmaps = {}
        filtered=[]
        for email in emails:
            dom = email.split('@')
            dom[0]=dom[0].replace('.','')
            if '+' in dom[0]:
                loc = dom[0].split('+')
                filtered.append(str(loc[0]+'@'+dom[1]))
            else:
                filtered.append(str(dom[0]+'@'+dom[1]))
        #print(filtered)
        
        for i in range(len(filtered)):
            if filtered[i] not in hmaps:
                hmaps[filtered[i]] = 1
        return(len(hmaps.keys()))

if __name__ == '__main__':
	emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	print(numUniqueEmails(emails))