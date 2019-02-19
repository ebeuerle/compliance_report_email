# RedLock compliance policy download and email 

Version: *1.0*
Author: *Eddie Beuerlein*

### Summary
This script will read a csv file to get a list of compliance report names and email addresses, contact the RL api and look for matches.  When a match is found, it will download the report and send it to the email recipent.  .

### Requirements and Dependencies

1. Python 2.7.10 or newer

2. OpenSSL 1.0.2 or newer

(if using on Mac OS, additional items may be nessessary.)

3. Pip

```sudo easy_install pip```

4. Requests (Python library)

```sudo pip install requests```

5. YAML (Python library)

```sudo pip install pyyaml```

### Configuration

1. Navigate to *compliance_report_email/config/configs.yml*

2. Fill out your RedLock username, password, and customer name - if you are the only customer in your account then leave this blank.

3. Populate the input.csv with the report names in RedLock and the email addresses you want the report sent to.

4. Customize the subject line if needed in runner.py

5. Customize the lib/email_helper.py to include the email server name/port, username/password, body and sender email address.

### Run

```
python runner.py

```
