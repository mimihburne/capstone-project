import re

def change_format(paragraph):
    indices = [i.start() for i in re.finditer('-', paragraph)]
    temp = list(paragraph)
    for j in indices:
        if re.search("[0-9]", temp[j-1]) != None and re.search("[0-9]", temp[j+1]) != None:
            temp[j] ='/'
    paragraph_new = ''.join(temp)
    return paragraph_new

#print(change_format('Please quote your policy number: 112-39-8552.'))

def validate(username):
    if len(username) >= 4: #at least 4 characters long
        if bool(re.match("^[A-Za-z0-9_]*$", username)) == True:
            if re.search('_{2,}', username) == None:
                if re.search('^[A-Za-z]', username) != None:
                    if re.search('_$', username) == None:
                        return True
        else:
            return False

print(validate('9ikeStandish'))