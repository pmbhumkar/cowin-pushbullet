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


### Install pushbullet library ###
Install pushbullet library using `pip install pushbullet.py`
 



## How to use ##
Add your pin code preferrences in config.json, pin_code data

Add your pushbullet access_token in get_vaccine.py
`API_KEY = "ADD_YOUR_API_KEY_HERE"`

Run the code as
`python3 get_vaccine.py`

## Sample Screenshot ##
![Notification Screenshot](https://github.com/pmbhumkar/cowin-pushbullet/blob/master/Screenshot_20210504-164141_Nova%20Launcher.jpg)
