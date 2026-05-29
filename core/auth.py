# core/auth.py
# using the Pygithub library to authenticate with GitHub
# source "https://github.com/PyGithub/PyGithub"

from github import Github, Auth
from dotenv import load_dotenv
import os


def authenticate_github():
    """Authenticates with GitHub using a personal access token stored in an environment variable (.env) and returns a Github instance."""

    # loading up .env file to access the GITHUB_TOKEN environment variable
    load_dotenv()

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not found in environment variables.")
        exit(1)

    try:
        # setting up authentication using a personal access token stored in an environment variable (.env)
        auth = Auth.Token(token)
        g = Github(auth=auth)
        user = g.get_user()
        return g
    except Exception as e:
        print(f"Authentication failed: {e}")
        exit(1)
