# Mass Mailer

A simple mass-mailer to send mails in bulk to lots of users at once.

## Steps to start using mass mailer

- Turn on the settings at https://myaccount.google.com/lesssecureapps to be able to send mails directly from your python code
- Run the following command on terminal in your mailer's folder

```
$ pip install -r requirements.txt
```

- Add a file named `config.py` in following format

```
sender_email = "xxxx@gmail.com"
sender_password = "xxxxxx"
```

- Add another file named `mail.xlsx` with all your emails that you need to send mails to under a column named `email`.

- Edit `message.py` according to your needs. A sample message has been provided, you don't have to use that.<br>
  NOTE: The message should be in HTML format

After all these steps, mass mailer is ready to be used!!
