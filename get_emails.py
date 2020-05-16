import json
import requests


username = '[Your username]'

# get token from https://github.com/settings/tokens
token = '[Your token]'

# creating  re-usable session object with user credentials
github_session = requests.Session()
github_session.auth = (username, token)

num =1

while num < 100 :
                      #replace to your organization name in place of microsoft 
 member_url='https://api.github.com/orgs/microsoft/members?page='+str(num)

#Get list of member 
 response = github_session.get(member_url)


#convert to json from requests and increase loop value
 response = response.json()
 num= num + 1

#get individual user membership information
 for values in response:
   userurl=values['url']
   response1 = github_session.get(userurl)

#get json from response1
   response1 = response1.json()


# from dictionary keys take email and print the value 
   for email in response1.keys():
    if email == 'email':
      print(response1.get(email))
      

