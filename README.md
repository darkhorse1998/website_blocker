# website_blocker
THIS IS A PYTHON CODE TO BLOCK WEBSITES FROM YOUR HOST PC.

Just add the list of websites to block in website dictionary.
Currently the restriction time is from 5-22 (5 AM - 10 PM). You can change it according to your wish.


----------------------------------
IMPORTANT
----------------------------------
1) Run the file with administrator privileges. Else you can't modify the host file on your PC with the script.
2) Make sure you backup a copy of your host files befor implementing any changes.


----------------------------------
Running as a background process
----------------------------------
Firstly, you need to rename the format of your python script to ".pyw", then you need to schedule a task and for that you need to follow the following Steps -

Step 1 : Go to START and search for "TASK SCHEDULER" , find and click on "CREATE TASK" you will get a popup and then in GENERAL section type the name you want to give to your task and Check the "RUN WITH HIGHEST PRIVILEGES" box, then move to Trigger panel.

Stepc 2 : Click on the "Begin the task" dropdown button and select "At startup". Then move to Actions panel.

Step 3 : Add a new "Action" and then in "Action" select "Start a new program" and add the file path to your python script. And then click OK and move to "Conditions" panel.

Step 4 : In "Conditions" panel uncheck the "Stop if the battery switches to battery power" option and you are good to go.

------------------------------
SCOPE FOR IMPROVEMENTS
------------------------------
1) A GUI can be created to ease the process of executing the job.
2) Currently the code is based to work according to the system's time. It needs to be changed to prevent a loophole.
3) A feature can be added to unblock the sites by removing the sites name from host files.
