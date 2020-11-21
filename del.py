import os
import requests
import re
import sys

#Replace the values with your data
user="enter c_user value from cookie"
xs="enter xs value from cookie"
dtsg="enter fb_dtsg value"
doc="enter doc_id here"

print('\n')
print('Before running this script, here are few things to consider:\n1) This script if used as it is, will:\n -unsend all your messages,\n -delete the \'you unsent a message\' messages and\n -delete conversation partner\'s messages\n2) If you just want to unsend your messages and nothing else, comment the lines: 98 and 108.\n3) If you want to unsend your messages and also want to remove the \'you unsent a message\' but not delete your partner\'s message, comment the line 108.\n4) If you want to unsend your messages and delete your partner\'s messages, but keep \'you unsent a message\' messages, comment line 98.')
print('\nScript By:  Prabesh Sapkota (sapkotaprabesh.github.io | prabeshsapkota.com.np | prabeshsapkota.info.np)')
print('\n\n\n')
continu = input('Press enter to continue..')
print('\n\n\n')

target=input('Enter target username or profile id (messenger.com/t/????): ')
if type(target) == int:
     print('\n')
else:   
    target = requests.post('https://www.facebook.com/'+target)
    target=str(target.text)
    poss=re.search("entity_id", target)
    if poss==None:
        sys.exit('Couldn\'t fetch profile id from username.\n Check if the provided target usename is correct and try again')
    target=re.findall("entity_id\":\"................",target)
    target=str(target)
    target=re.sub(r'\D','',target)
print('\n\n\n')

cookies = {
    'c_user': user,
    'xs': xs,
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded, application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0',
}

data = {
  'batch_name': 'MessengerGraphQLThreadFetcher',
  '__user': user,
  '__a': '1',
  'fb_dtsg': dtsg,
  'queries': '{"o0":{"doc_id":'+doc+',"query_params":{"id":'+target+',"message_limit":20000000000000000}}}'
}

response = requests.post('https://www.messenger.com/api/graphqlbatch/', headers=headers, cookies=cookies, data=data)
out=response.text
#sys.exit(out)
clse=re.search('Please try closing and re-opening your browser window.', out)
if clse!=None:
    sys.exit('Please check if the dtsg value is correct.\n If you continuously get this error, uncoment line 53 and run the script again and send me the output at prabesh01@pm.me')
exp=re.search('Please log in to continue.', out)
if exp!=None:
    sys.exit("Please check if cookies value is up-to-date.\n If you continuously get this error, uncoment line 53 and run the script again and send me the output at prabesh01@pm.me") 
sth=re.search('mid', out)
if sth==None:
    sys.exit("Something went wrong, Please try again.\n If you continuously get this error, uncoment line 53 and run the script again and send me the output at prabesh01@pm.me")   
     
x=re.findall('mid\.\$.............................',out)
x = list(dict.fromkeys(x))
total=len(x)

for count in reversed(range(total)): 
    cookies = {
    'c_user': user,
    'xs': xs,
    }

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0',
    }

    data = {
   'message_id': str(x[count]),
   '__user': user,
   '__a': '1',
   'fb_dtsg': dtsg
    }

    response = requests.post('https://www.messenger.com/messaging/unsend_message/', headers=headers, cookies=cookies, data=data)
    last=response.text
    den=re.search("errorSummary", last)
    if den==None:
         print('-\n-\n-\n-\n-\n'+str(count)+'/'+str(total)+":\nDone\n")
         data = {
          'message_ids[0]': str(x[count]),
          '__user': user,
          '__a': '1',
          'fb_dtsg': dtsg
        }

         requests.post('https://www.messenger.com/ajax/mercury/delete_messages.php', headers=headers, cookies=cookies, data=data)
    if den!=None:
         print('-\n-\n-\n-\n-\n'+str(count)+'/'+str(total)+":\nDone\n") 
         data = {
          'message_ids[0]': str(x[count]),
          '__user': user,
          '__a': '1',
          'fb_dtsg': dtsg
        }

         requests.post('https://www.messenger.com/ajax/mercury/delete_messages.php', headers=headers, cookies=cookies, data=data)    

    #for debug purpose:
    #print('-\n-\n-\n-\n-\n'+str(count)+'/'+str(total)+":\nRequest:\n"+str(response.request.headers)+'\n'+str(response.request.body)+"\n\nResponse:\n"+str(response.text))
sys.exit('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCompleted Sucessfully!')
