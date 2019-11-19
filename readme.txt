Go to https://myaccount.google.com/apppasswords and generate an app password for this. Under select app, you can say custom and set it to Secret Santa. For device select Mac (or windows or linux) depending on what OS you run the script from. Save the generated password.

Update your environment variables to include the app password generated and your email account. For example in my bash_rc I have:

export SECRET_SANTA_PASS="password_copied_from_website"
export SECRET_SANTA_EMAIL="yazzy.latif@gmail.com"

Be sure to download a tsv. The format of the file should be 

name \t email \t likes ...

If you have more columns after likes be sure to update the format_email function in the santa.py file. Also feel free to change the email to say whatever you want!

Then run 

python santa.py --input name_of_input_file.tsv --output name_of_output.txt -s (set this if you want to send)