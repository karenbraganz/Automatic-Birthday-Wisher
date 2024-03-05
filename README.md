<p>Are you terrible at reviewing your calendar daily and worse at remembering birthdays? This birthday-wisher might be the perfect tool for you!</p>

<h3>Overview</h3>
<p>This birthday-wisher ensures that you never miss wishing your friends and family on their birthdays. It can read a .csv file which contains data about the birthdays and emails of your friends and family and automatically send them an email greeting on your behalf if it is their birthday.</p>

<h3>Setup: </h3>
<ol>
  <li>
    <p>After downloading all files in this repository, you may set up an app password on your email account for birthday-wisher. This will allow birthday-wisher to automatically send emails on your behalf. The following links contain information about setting up app passwords on Gmail, Outlook, and Yahoo:</p>
    <ul>
      <li><a href="https://support.google.com/mail/answer/185833?hl=en">Gmail</a></li>
      <li><a href="https://support.microsoft.com/en-us/account-billing/create-app-passwords-from-the-security-info-preview-page-d8bc744a-ce3f-4d4d-89c9-eb38ab9d4137">Outlook</a></li>
      <li><a href="https://help.yahoo.com/kb/SLN15241.html">Yahoo</a></li>
    </ul>
  </li>
  <li>
    <p>Create a .env file within the same directory as the main.py file. You may store the environment variables containing your email address and app password within this file for main.py to load while running. You may copy the contents of the env.placeholder file from this repository into your .env file and replace the email and app password data appropriately.</p>
  </li>
  <li>
    <p>Edit the birthdays.csv file to include the names, emails, and birthdays of your friends and family.</p>
  </li>
  <li>
      <p>You may use <a href="https://www.pythonanywhere.com/">Python Anywhere</a> to automate your script to run daily. You would have to upload all files to Python Anywhere and schedule a task to run the main.py file daily as described <a href="https://help.pythonanywhere.com/pages/ScheduledTasks/">here</a>. The relative locations of all files should be maintained as these relative paths are referenced in main.py.</p>
  </li>
</ol>
