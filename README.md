# gitbandit

**Proving that "commit productivity" is a scam, one automated green square at a time.**

Long story short: I don't like people who measure productivity and learning by how many commits you make. It's the exact same energy as measuring developer skill by asking, "how many lines of code did you write today?" 

So, **FORK THAT**. I automated that BS(kinda of). Mwahahahah.

*(Anyways, this was cooler in my head, ngl).*

---

## Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/piratebird/gitbandit.git
cd gitbandit
```

**2. Set up your Python Virtual Environment**
Keep your system packages clean. 
```bash
python3 -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate  

# Activate it (Windows)
# venv\Scripts\activate   
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure your GitHub Token**
Gitbandit needs a Personal Access Token (PAT) to work its magic.
1. Go to GitHub -> **Settings** -> **Developer Settings** -> **Personal access tokens** -> **Tokens (classic)**
2. Generate a new token. Ensure you check the **`repo`** scope (Full control of private repositories).
3. Copy the `.env.example` file and rename it to `.env`.
4. Paste your token inside:

```env
# Inside your .env file
GITHUB_TOKEN=your_personal_access_token_here
```

---

## Usage (WIP)

Once your environment is set up, just run the main script. It will ask for your target repository and handle the rest (creating the repo if it doesn't exist, and committing so hell yeah :b ).

```bash
python __main__.py
```

> *Pro-tip for automation: Instead of leaving a Python script running 24/7 in the background, set up a native `crontab` or a `systemd` timer to run this script daily.*

---

## Roadmap (Features to add when I'm less lazy prolly)

- [ ] **Time Traveler:** Spoofing `GIT_AUTHOR_DATE` to commit into the past.
- [ ] **Better UX:** Polish up the CLI interactions.
- [ ] **The "Green Square" Canvas:** Build a TUI to actually *draw* specific shapes on the GitHub contribution graph using targeted commits.
- [ ] **Engine Swap:** Possible implementation of the native `subprocess` library instead of `PyGithub` (or make it a user choice).
- [ ] **Built-in Scheduler:** Solve the dilemma between `crontab` vs. `systemd-service` vs. a Python script running 25/8.
- [ ] *Idk, if any other idea comes to mind Imma add it here.*

---

## License

This project is licensed under the GPL License.
See the [LICENSE](LICENSE) file for details.