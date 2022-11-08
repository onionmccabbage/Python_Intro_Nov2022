# when we get remote data we should:
# validate
# check against errors

# this time we will use the following URL
# https://api.first.org/data/v1/teams/

import requests # we need this!!

def main():
    url = 'https://api.first.org/data/v1/teams/'
    # url = 'http://broken.ie'
    # try to make a call to the URL
    try: # it is always a good idea to wrap requests in 'try' and 'except'
        result = requests.get(url)
        return result.json() # this is only rerturned if the request was successful
    except requests.ConnectionError as err: # capture request errors
        print('Problem with end-point: {}'.format(err))
    except Exception as err: # capture more generic errors
        print('something went wrong: {}'.format(err))
    finally:
        pass # we could tidy up here...

if __name__ == '__main__':
    j = main()
    print(j['status'])
    print(j['data'][0]['country'])