import requests
import argparse
import sys
    
def command_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', '-k', help='API Key')
    parser.add_argument('--token', '-t', help='Trello Token')
    parser.add_argument('--board_id','-id', help='ID of the Trello Board to which card has to be added')
    parser.add_argument('--list_name', '-l', help='Name of the list to which card has to be added [TO DO, DONE, DOING]')
    parser.add_argument('--card_name', '-n', help='Name of the card')
    parser.add_argument('--labels', nargs='*', default=[], help='Label colours')
    parser.add_argument('--comment',  default=None, help='Comment on the card')
    
    return parser.parse_args()

def authentication(API_Key,Token,id,list_name,card_name,labels,comment):
    url = "https://api.trello.com/1/members/me/boards"

    query = {
    'key': API_Key,
    'token': Token
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )
    #print(response.text)
    if response.status_code == 200:
        #Check for authenticity of Board ID
        board_id_check(id,list_name,card_name,labels,comment,API_Key,Token)

    else:
        print('Invalid API Key or Token')
        sys.exit(1)

def board_id_check(API_Key,Token,id,list_name,card_name,labels,comment):
    url = "https://api.trello.com/1/boards/{id}/memberships"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': API_Key,
    'token': Token
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )
    if response.status_code == 200:
        #Proceed to add card after verifying all details
        add_card(id,list_name,card_name,labels,comment,API_Key,Token)

    else:
        print('Invalid Board ID')
        sys.exit(1)


def get_listid(API_Key,Token,id,list_name):
    try:
        url = f"https://api.trello.com/1/boards/{id}/lists"

        headers = {
        "Accept": "application/json"
        }

        query = {
        'key': API_Key,
        'token': Token
        }

        response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
        )

        lists = response.json()
        for i in lists:
            # To Handle case sensitivity and spacing of list names
            if i['name'].replace(" ", "").lower() == list_name.replace(" ", "").lower():
                #print(i['id'])
                return i['id']
    except:
        return None
    
def add_card(id, list_name, card_name, labels, comment, API_Key, Token):
    #Get list id using name of the list
    list_id = get_listid(API_Key,Token,id,list_name)

    if list_id:
        url = "https://api.trello.com/1/cards"

        headers = {
        "Accept": "application/json"
        }

        query = {
        'idList': list_id,
        'key': API_Key,
        'token': Token,
        'name': card_name
        }

        response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
        )

        card_id = response.json().get('id')
    
    else:
        print('No list with the give name found. Give a valid list name')
        sys.exit(1)


    if labels:
        url = f"https://api.trello.com/1/cards/{card_id}/Labels"
        #print(labels)
        for label in labels:
            query = {
            'key': API_Key,
            'token': Token,
            'color': label
            }

            response = requests.request(
            "POST",
            url,
            params=query
            )


    if comment:
        url = "https://api.trello.com/1/cards/{id}/actions/comments"

        headers = {
        "Accept": "application/json"
        }

        query = {
        'text': comment,
        'key': API_Key,
        'token': Token
        }

        response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
        )

    print(f"Card '{card_name}' added successfully")



def main():
    args = command_parser()
    #Parse arguments from command given by user
    api_key = args.key
    token = args.token
    board_id = args.board_id
    list_name = args.list_name
    card_name = args.card_name
    labels = args.labels
    comment = args.comment

    if api_key is None or token is None:
        print('No API_KEY or API_Token Provided')
        sys.exit(1)

    #Authenticate Credentials
    authentication(api_key,token,board_id,list_name,card_name,labels,comment)


if __name__ == "__main__":
    main()

