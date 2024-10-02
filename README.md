## Trello Card CLI
This Python script creates cards, assigns labels and adds comment from the command line to the specified list on trello board.

## Requirements
* Python3
* Trello API Key and Token(Can be generated at https://trello.com/power-ups/admin/new )
* Board ID (It can be found after clicking the board and adding '.json' at the end of the URL. The value we need is "id" at the start of JSON.)

## Usage
- Install the requirements using the command
   * pip install -r requirements.txt

- Run the script with any of the following commands with necessary arguements :
   * python Trello.py --key 'API KEY' --token 'TOKEN' --board_id 'id' --list_name "List Name" --card_name "Name" --labels Colour1 Colour2 --comment "Comment"
   * python Trello.py -k 'API KEY' -t 'TOKEN' -id 'id' -l "List Name" -n "Name" --labels colour1 colour2 -c "Comment"

- To avoid repetition and ensure security, it’s ideal to store API keys and tokens in/as environment variables

## Error Handling
- Implements error handling for various issues faced during development
- Includes checks for API authentication, failed API requests, null credentials, incorrect list names and board IDs
- Takes care of edge cases such as missing parameters and irregular command arguments 

## Help
* Run `python Trello.py -h` to see the help message



## Future Development
I want to expand the Trello CLI tool to work more like 'kubectl' for Kubernetes. I would more features so the tool can provide a full view and control of resources, such as listing and creating boards, viewing, creating or moving lists within boards and viewing or adding details like comments and labels for each list. I believe this will make it more user friendly for managing Trello directly from the command line


## References
I have used the following resources to complete this task :-
- PixieBrix Documentation(https://docs.pixiebrix.com/integrations/trello)
- Trello REST API Docs(https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-group-actions)
- Command Line Blog(https://www.kdnuggets.com/build-a-command-line-app-with-python-in-7-easy-steps)








