# Productivity Pet
A CEN3101 Project by Urmi Thorat, Yanna Lin, Michael Cardei, and Saketh Renangi
## Description 
The pandemic has led to a higher dependence and use of online learning. This unprepared shift in the education system has created challenges. One of these challenges includes decreased student engagement. Productivity Pet provides a solution to this issue.

The Productivity Pet is a Canvas-integrated desktop pet application that helps students with schedule management and staying productive. The software displays on a desktop screen as a desktop pet, with additional functionality. The pet sits on top of a clock, allowing a user to keep track of time. By pressing the _Options_ button, each user can view their individual Canvas assignments, input additional assignments manually, and set reminders for themselves.
## Getting Started
Begin by cloning this repository onto a personal device or downloading the zipped files. 
The Python language must be available, along with the following packages must be installed: _collection_, _operator_,_random_, _time_, _tkinter_, _datetime_, _functools_,  _canvasapi_, _pymongo_, _pymongo[srv]_, and _pytz_. These packages can be installed by running `pip install _package name_`or `pip3 install   _package name_`, depending on your Python version, on your device, on the IDE or device terminal.


The desktop pet software is activated by running the Pet.py file within the pet directory. Once the pet appears on the desktop monitor, press the _Options_  button. In doing so, a GUI will appear on the screen. Inputting a personal Canvas API key and pressing the _Connect to Canvas_ produces the dialogue on the IDE or terminal used to run Productivity Pet. More information on creating a Canvas API key can be found below. By providing responses to this additional dialogue, a user profile has been created. The name inputted by the user during this point can be used at a future point for logging into the pet and accessing the task list.  The _Options_ button also allows for users to manually input tasks, create reminders, change the pet’s appearance, and print sorted tasks. Pressing the button labeled _Exit_ will quit the software.
## Creating a Canvas API Key
1. Log into your institution's Canvas web page.
2. Click on your profile in the upper left corner and select _Settings_.
3. Press the _+ New Access Token_ button and input   Productivity Pet   in the   Purpose   text edit. Leave _Expiration_ blank.
4. Copy the provided API key for use in the Productivity Pet.
## Contributions. 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. Currently, tests are found in the   Backend  directory. 
## License
[MIT](https://choosealicense.com/licenses/mit/)
