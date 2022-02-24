import whois

domain = whois.whois("https://www.giridhar.com/")
if domain == None:

    print("domain is not yet registerd")

else:
    print("domain is registered")
