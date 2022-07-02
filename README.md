# my-budget
I got fed up with the budgeting software out there and decided to make my own. So, with the help of my trusty Raspberry Pi, here is what I would like to do with this project:

## MVP
1. For every run, download the current version of the spreadsheet, check it into version control, and push it
2. Send text messages 1 day before bills or credit card posting and payments are due
3. 

## Basic Process
1. Enable the Pi to send and receive SMS
2. Enable the Pi to receive SMS regarding the Date, Withdrawl/Deposit, Category, and Description of a transaction
3. Enable the Pi to enter the data in step 2 into a google sheet
4. Enable the Pi to manipulate the google sheet in step 3 to create a nice chart (or pivot table) of our spending
5. Enable the Pi to update the charts (or pivot tables) on the google sheet every month so that there will be a view of the current month, all months in the year, and all years it has been logging

## Additional Feature Ideas
* Email a spreadsheet each morning and text each person reminding them of the email
* Create a backup of the spreadsheet each day (might not be neccessary if it is in the cloud as is the case of google sheets but still might be nice)
* Make it so it will email or text out a copy of the spreadsheet or a link to an identical google sheets (maybe sync them? Maybe have 2 at all time?)
* Return future expenses for a given date range
* Return net (all income - all expenses) for a given range
* format chart tab
* Compute Net Worth
* Use api to get bank balance information
* Use JSON to configure tables
