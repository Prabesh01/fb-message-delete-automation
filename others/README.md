# React Automation:
It will just react to all the messages of a conversation. The setup is same as the one in del.py expect the doc_id. doc_id is just a request id which is different for different kind of request. Since react needs totally different request than fetching mssg_ids, its doc_id is different. The doc_id is same for all the requests of same kind though.

### Setup
As mentioned earlier, the setup is same as in del.py. The only new thing to do is get one more doc_id. The doc_id used in del.py is for fetching messages_id. The doc_id for reacting to the messages is different. To find it, just open messenger.com then fireup burp and intercept req while reacting to any message. You would the get the doc_id in the intercepted request body.

- Insert the obtained doc_id at line 10 and the doc_id used in del.py (the doc_id for fetching messages_ids) in line 46. 

- Choose what emoji to be used in line 82. Replace 😇 with whatever emozi you want to use. You may copy emoji from <a href="https://www.emojicopy.com/">here</a> or <a href="https://getemoji.com/">here</a>

_In order to reverse the process (i.e. remoove certain emozi from all messages), just replace ADD_REACTION with REMOVE_REACTION in line 82._
