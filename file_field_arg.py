from jira import JIRA
import sys

def update_jira_field(username, password, jira_ticket, field_value):
    options = {
        'server': 'https://your-jira-instance.com'
    }

    jira = JIRA(options, basic_auth=(username, password))

    issue = jira.issue(jira_ticket)
    issue.update(fields={'customfield_17856': field_value})
    print(f"Field 'customfield_17856' updated successfully for {jira_ticket}")

if len(sys.argv) != 4:
    print("Usage: python script.py <username> <password>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
jira_ticket = 'YOUR_JIRA_TICKET'
field_value = 'YOUR_FIELD_VALUE'  # Fetch the field value from Jenkinsfile using os.environ.get()

update_jira_field(username, password, jira_ticket, field_value)
