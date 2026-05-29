# core/commiter.py
# module that handles the logic for updating or creating a file in the GitHub repository using the PyGithub library

from github import GithubException


def update_or_create_file(repo,file_path="bandit_log.txt", commit_message="Automated update by gitbandit", content="This is an automated update by gitbandit."):
    """Updates an existing file or creates a new file in the repository with a commit message and content."""

    commit_message = f"Automated update to {file_path} by gitbandit"
    
    try:
        file_contents = repo.get_contents(file_path)
        existing_text = file_contents.decoded_content.decode("utf-8")
        new_text = existing_text + "\n" + content

        repo.update_file(
            path=file_path,
            message=commit_message,
            content=new_text,
            sha=file_contents.sha,
            branch="main",
        )
        print(f"Successfully updated '{file_path}' in the repository.")

    except GithubException as e:
        if e.status == 404:
            print(f"'{file_path}' not found. Creating a new file.")

            repo.create_file(
                path=file_path,
                message=commit_message,
                content=content,
                branch="main",
            )
            print(f"Successfully created '{file_path}' in the repository.")
        else:
            raise e
    except Exception as e:
        print(f"Error occurred while updating or creating file: {e}")
