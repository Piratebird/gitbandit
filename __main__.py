# the main entry of the script

###--- IMPORTS ---###
from core.auth import authenticate_github
from core.commiter import update_or_create_file
from core.repo_manager import get_or_create_repo
import random
import time

##--- MAIN FUNCTION ---#
def main():
    try:
        # authenticate with GitHub and get a Github instance
        g = authenticate_github()
        user = g.get_user()
        print(f"Authenticated as: {user.login}")

        # get repo name from user input or use a default value
        repo_name = input(
            "Enter the repository name (format: 'username/repository'): "
        ).strip()
        if not repo_name:
            # specify the repository to update or create the file in (format: "username/repository")
            repo_name = f"{user.login}/gitbandit-auto-commits"
            print(f"No repository name provided. Using default: {repo_name}")
        else:
            print(f"Using repository: {repo_name}")

        # get or create the repository using the provided name
        repo = get_or_create_repo(g, repo_name)
        # get the number of commits to make from user input or use a default value of 5
        max_commits_input = input(
            "Enter the number of commits to make (default is 5): "
        ).strip()

        # convert the input to an integer if it's a valid number, otherwise use the default value of 5
        max_commits = int(max_commits_input) if max_commits_input.isdigit() else 5

        # commit the day keep the doctor away, or something like that
        for i in range(max_commits):
            print(f"Making commit {i + 1} of {max_commits}...")
            # simulate some work by sleeping for a random amount of time between 1 and 3 seconds
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            unique_content = (
                f"This is an automated update by gitbandit at {current_time}."
            )

            # update or create the file in the repository with the unique content for each commit
            update_or_create_file(repo, content=unique_content)
            if i < max_commits - 1:  # only sleep if there are more commits to make

                # also sleeping to not fuck the github api limit
                time.sleep(random.uniform(1, 3))

    # catching errors like pokemons
    except Exception as e:
        print(f"An error occurred: {e}")

    # gotta catch 'em all
    except KeyboardInterrupt:
        print("\nProcess interrupted by the gobo, Exiting gracefully perchance.")
        exit(0)


# main door ig
if __name__ == "__main__":
    main()
