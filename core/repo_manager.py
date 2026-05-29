# core/repo_manager.py
# module that manages the github repos

from github import GithubException


def get_or_create_repo(g, repo_name, private=True):
    """
    Attempts to fetch a repository. If it doesn't exist, it creates it.
    Requires the authenticated Github object (g) and the target repo name.
    """

    try:
        # try to get the repo if it exists
        repo = g.get_repo(repo_name)
        print(f"Repository '{repo_name}' found.")
        return repo  # return the repo if it exists

    except GithubException as e:
        if e.status == 404:
            print(f"Repository '{repo_name}' not found. Creating a new repository.")

            # to create a repo we need the authenticated user, so we get the user from the Github instance and then create the repo under that user
            user = g.get_user()
            clean_name = repo_name.split("/")[
                -1
            ]  # extract the repo name from the full repo name (username/repo)
            repo = user.create_repo(name=clean_name, private=True)
            print(f"Repository '{repo_name}' created successfully.")
            return repo  # return the newly created repo
        else:
            print(f"Error occurred while fetching or creating repository: {e}")
            raise e
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e
