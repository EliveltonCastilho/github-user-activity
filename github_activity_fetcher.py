import requests
from datetime import datetime

def fetch_github_user_events(username):
    url = f'https://api.github.com/users/{username}/events'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"\n❌ Error: User '{username}' not found.\n")
        elif response.status_code == 403:
            print(f"\n❌ Error: API rate limit exceeded. Please try again later.\n")
        else:
            print(f"\n❌ HTTP Error occurred: {http_err} (HTTP {response.status_code})\n")
        return None
    except requests.exceptions.RequestException as err:
        print(f"\n❌ Error: A problem occurred while trying to fetch data: {err}\n")
        return None

    return response.json()

def format_event_time(timestamp):
    event_time = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    return event_time.strftime('%B %d, %Y at %I:%M %p')

def print_github_events(events, username):
    if not events:
        print(f"\nℹ️ No recent events found for user '{username}'.\n")
        return
    
    print(f"\n📊 Recent Activity for GitHub User: {username}\n")
    print("="*50)
    
    for event in events[:5]:  # Limiting to the 5 most recent events for brevity
        event_time = format_event_time(event['created_at'])
        print(f"📝 Event Type: {event['type']}")
        print(f"📂 Repository: {event['repo']['name']}")
        print(f"⏰ Created At: {event_time}")
        
        if event['type'] == "WatchEvent":
            print(f"⭐ Action: {event['payload']['action']}")
        elif event['type'] == "PushEvent":
            for commit in event['payload']['commits']:
                print(f"🔗 Commit SHA: {commit['sha']}")
                print(f"✍️ Author: {commit['author']['name']}")
                print(f"💬 Message: {commit['message']}")
                print(f"🔗 URL: {commit['url']}")
        
        print("-" * 50)
    
    print("\nEnd of Report\n")

def main():
    print("🔍 Welcome to the GitHub User Activity Fetcher 🔍\n")
    username = input("Please enter the GitHub username: ").strip()
    
    if not username:
        print("❌ Error: Username cannot be empty.\n")
        return
    
    events = fetch_github_user_events(username)
    
    if events:
        print_github_events(events, username)
    else:
        print("No events to display.\n")

if __name__ == "__main__":
    main()
