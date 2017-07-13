def palindrome(s):

        t=""
        for i in range(0,len(s)):
                if s[i]=="A":
                        t=t+"T"
                if s[i]=="T":
                        t=t+"A"
                if s[i]=="G":
                        t=t+"C"
                if s[i]=="C":
                        t=t+"G"
        x=t[::-1]
        if x==s:
                return "It is a palindrome"
        else:
                return "It is not a palindrome"


