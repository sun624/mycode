#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
num_get = 0
num_post = 0
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        if "GET" in line:
            num_get += 1
        if "POST" in line:
            num_post += 1
print("The number of failed log in attempts is", loginfail)
print("The number of GET and POST requests is",num_get,num_post)


