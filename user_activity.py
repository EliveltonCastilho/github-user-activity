import requests
from datetime import datetime

def fetch_github_user_events(username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"\n❌ Error: Could not fetch events for user '{username}' (HTTP {response.status_code})\n")
        return None

def format_event_time(timestamp):
    event_time = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    return event_time.strftime('%B %d, %Y at %I:%M %p')

def print_github_events(events, username):
    if not events:
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
    username = input("Please enter the GitHub username: ")
    events = fetch_github_user_events(username)
    
    if events:
        print_github_events(events, username)
    else:
        print("No events to display.\n")

if __name__ == "__main__":
    main()
