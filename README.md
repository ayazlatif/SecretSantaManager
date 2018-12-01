<h1>Secret Santa Manager</h1>
 

<h2>FORMAT OF FILES</h2>

<p>Make sure you format the secret santa files as follows:</p>

<p>Name | email | interests/likes</p>

<p>You may add more categories if you like, but you will have to modify the santa.py. 
Modify the format_email function if your file is formatted differently. 
It is easiest if name and email are still first, you may have to change the code in a few other places
if name and email aren't the first 2. </p>

<p>The assignments file is what will keep track of who all the secret santas were. 
The format is as follows:</p>

<p>
gifter, reciever<br>
gifter2, reciever2<br>
...
</p>


<h2>INSTALLATION</h2>
<p>This file requires the use of the google api. You will need to set up API keys yourself if you want to use this code.</p>

<p>This requires Python 3 install that first
If you are on mac you also need pip to install run on terminal</p>

<code>sudo easy_install pip</code>

<p>Now you need the google api go ahead and use this </p>
<code>pip3 install --upgrade google-api-python-client oauth2client</code>

<p>You also need retrying (handles error code 500 hopefully!!)</p>
<code>pip3 install retrying</code>

<h2>HOW TO RUN</h2>

<p>Inside santa.py:<br>
Adjust the constant SEND if you want to send out the messages or test it out.</p>

<p>Adjust the YOUR_EMAIL constant to be the email you authorized when you run the command at the end of this read me. </p>

<p>Adjust the INPUT constant to be the your secret santa file described above.</p>

<p>Adjust the OUTPUT constant to be the assignments file described above.</p>

<p>To run the program use in terminal</p>
<code>python3 santa.py</code>

