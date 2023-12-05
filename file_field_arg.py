from jira import JIRA
import sys
import os

def update_issue_field(username, password, issue_key, field_id, new_value):
    jira_url = "https://jira.charter.com"

    try:
        jira = JIRA(server=jira_url, basic_auth=(username, password))
        issue = jira.issue(issue_key)

        # Prepare the update field dictionary
        update_fields = {field_id: new_value}

        issue.update(fields=update_fields)

        print(f"Field '{field_id}' in issue '{issue_key}' updated successfully to '{new_value}'.")
    except Exception as e:
        print(f"Failed to update the field '{field_id}'. Error:", str(e))

# Check if correct number of arguments is provided
if len(sys.argv) != 3:
    print('Usage: python script.py username password')
    sys.exit(1)

# Username and password from command line arguments
username = sys.argv[1]
password = sys.argv[2]

jiraTicket = os.environ.get('JIRA_TICKET')
artifactId = os.environ.get('Artifact_id')  # Fetching the Artifact_id environment variable

# Define the specific Jira field ID here (e.g., customfield_17856)
custom_field_id = 'customfield_17856'

update_issue_field(username, password, jiraTicket, custom_field_id, artifactId)
