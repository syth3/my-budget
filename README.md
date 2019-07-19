# my-budget
I got fed up with the budgeting software out there and decided to make my own. So, with the help of my trusty Raspberry Pi, here is what I would like to do with this project:

## Basic Process
1. Enable the Pi to send and receive SMS
2. Enable the Pi to receive SMS regarding the Date, Withdrawl/Deposit, Category, and Description of a transaction
3. Enable the Pi to enter the data in step 2 into a google sheet
4. Enable the Pi to manipulate the google sheet in step 3 to create a nice chart (or pivot table) of our spending
5. Enable the Pi to update the charts (or pivot tables) on the google sheet every month so that there will be a view of the current month, all months in the year, and all years it has been logging

## Additional Feature Ideas
* make it so it will email the spreadsheet each morning and text each person reminding them of the email
* make it so it will create a backup of the spreadsheet each day (might not be neccessary if it is in the cloud as is the case of google sheets but still might be nice)
* Make it so it will email or text out a copy of the spreadsheet or a link to an identical google sheets (maybe sync them? Maybe have 2 at all time?)
* Return future expenses for a given date range
* Return net (all income - all expenses) for a given range
* format chart tab
* Compute Net Worth
* Use api to get bank balance information
