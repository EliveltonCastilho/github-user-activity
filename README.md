# github-user-activity

Sample solution for the [github-user-activity](https://roadmap.sh/projects/github-user-activity) challenge from [roadmap.sh](https://roadmap.sh/).


## Features

- Fetches up to 5 recent events for a GitHub user.
- Handles errors gracefully, including invalid usernames and API rate limits.
- Displays events in a clean and readable format.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/EliveltonCastilho/github-user-activity.git
    cd github-user-activity
    ```

2. Ensure you have Python 3 installed.

3. Install the required Python library:

    ```bash
    pip install requests
    ```

## Usage

1. Run the script using Python:

    ```bash
    python github_activity_fetcher.py
    ```

2. Enter the GitHub username when prompted:

    ```bash
    🔍 Welcome to the GitHub User Activity Fetcher 🔍

    Please enter the GitHub username: octocat
    ```

3. The script will fetch and display the user's recent activity.

## Error Handling

- If the user does not exist, you will see an error message.
- If the API rate limit is exceeded, the script will inform you to try again later.

## Project Page

For more details about the project and to view the roadmap, visit the [project page](https://roadmap.sh/projects/github-user-activity).

## Contributing 

Feel free to fork this repository and submit pull requests. Contributions are welcome!
