# cowin-pushbullet #
User will receive a push bullet for available slot

## Pre-requisite ##
### Create a pushbullet access token ###
* Go to https://www.pushbullet.com
* Download pushbullet app on your respective device (Android/Iphone)
* Login with the google/facebook
* On Webpage, verify that the _set up your phone_ is ticked
* Go to Settings -> Create access token
* Copy this access token as this will be needed in the code


### Packages dependencies ###
* Pushbullet
	* Install pushbullet library using `pip3 install pushbullet.py`
* fake-headers
	* Install using `pip3 install fake-headers`

_Note: Added requirements.txt file that can be used to complete dependencies installation_  
`pip3 install -r requirements.txt`
 

## How to use ##
Edit config.json file for following
* api_key: Pushbullet access_token
* pincode: Add your preferrenced area pincode in a list
* age: Add 18 for 18+ vaccines, and 45 for 45+ vaccines in a list (both can also be added for all search)
* timeday: The recurrence of the script execution, in seconds

Run the code as
`python3 get_vaccine.py`

## Sample Screenshot ##
![Notification Screenshot](https://github.com/pmbhumkar/cowin-pushbullet/blob/master/Screenshot_20210504-164141_Nova%20Launcher.jpg)
