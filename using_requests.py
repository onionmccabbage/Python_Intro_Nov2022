import requests

# we will use the 'requests' library to make calls to an HTTP API end-point
# https://jsonplaceholder.typicode.com/users/

def getData(whichID=1): # we expect an argument, but give it a default
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(whichID)
    # we can make requests to this end-point API and store the results
    # the 'requests' library already has a 'get' method
    r = requests.get(url) # here we ask for the JSON available at this URL
    # remember the JSON is text, so we need ot convert it to a Python structure
    r_dict = r.json() # convert the text to a list or dictionary
    return r_dict

if __name__ == '__main__':
    # ask which id is needed
    q = input('Please enter a number 1-10 ')
    q_num = int(float(q)) # make sure it is an integer
    users = getData(q_num) # here we can choose to inject a value for 'whichID'
    # break out the parts of the data we are interested in
    user_name = users['name']
    user_email = users['email']
    user_street = users['address']['street']
    # show a nicely formatted result
    # NB each curly-bracket matches up to one of the items in the 'format'
    #               0               1             2            0          1          2
    print('Name is {} and email is {}, living on {}'.format(user_name, user_email, user_street))
    print( users, type(users) )