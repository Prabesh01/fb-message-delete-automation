# Doesn't work anymore from Jan 10 2021
_will try to update the script to make it work with new messsenger updates_

This script is still in beta version, not because its not working well but because its hard to setup for the first time. But once you set it up, you are ready to go. I will improve this script to set it up by itself in future.

<img alt="Demo" src="demo.png" />

# Setup

To set it up, you will need to provide 4 values to the script so that this script could perform actions on behalf of you. They are : c_user, xs, fb_dtsg and doc_id. These values doesn't change until your cookie renews. Here's how you could obtain them:

The value of user and xs can be found in cookies by name c_user and xs respectively.
The dtsg value can be obtained by running this code in messenger.com's console:
```
var dtsg = require('DTSG').getToken();
  alert('Your fb_dtsg token: ' + dtsg);
  ```

To get doc_id value, simply open developer console's network tab in messenger.com and filter out /api/graphqlbatch/. You will probably get 3 results. The required doc_id can be found in the request containing data: batch_name="MessengerGraphQLThreadFetcher" like this:
<br>

<img alt="request sample" src="docid.png" />

<a href="https://github.com/TheBinitGhimire">@TheBinitGhimire</a>,<a href="https://www.facebook.com/nepolian.pratik">@nepolian.pratik</a>, <a href="https://github.com/santoshbrl5/">@santoshbrl5</a>, <a href="https://github.com/roopeshach">@roopeshach</a><br>
Thank you guys for helping me out =)

# Alternative

Alternatively, you can simply paste this script in messenger.com's console:
```
function ok(){
threedots = document.querySelectorAll("._8sop");
threedotslast = threedots[threedots.length - 1];
threedotslast.click();
removebutton = document.querySelector("._hw5");
removebutton.click();
unsendbutton = document.querySelectorAll("._3quh")[1];
unsendbutton.click();
setTimeout( ok, 1000 );
}
ok(1);
```
Ofcourse, it is limited and has many issues.

# License

[![CC0](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)
