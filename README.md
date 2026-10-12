# Kharazmi Agent

**Current version: `v0.1`** · [View releases](https://github.com/sobhsafa31-afk/Kharazmi-agent/releases)

Kharazmi Agent is a Python-based desktop assistant for Windows. It connects a language model to a set of local tools, allowing users to interact with selected file-system and system-information tasks through natural language.

> **Version status:** `v0.1` is the project's current version. The project team reports that all tests performed for this version passed. This statement reflects the team's report; it is not an independent audit.

## Features

Depending on the tools enabled in the current source code, Kharazmi Agent can:

- List files in a directory.
- Create folders and text files.
- Read text files and search for files.
- Open folders and supported applications.
- Report basic RAM and disk-usage information.
- Store recent conversation messages and simple long-term memory in SQLite.
- Use text-to-speech functionality where configured.

Available actions are determined by the tools implemented in the project. Not every feature is necessarily enabled in every version.

## Requirements

- Windows is recommended because some functions use Windows-specific behavior such as `os.startfile`.
- Python 3.10 or later is recommended.
- An internet connection for requests to the configured AI service.
- An API token from the AI provider used by the project.
- The account or project identifier required by that provider, if applicable.

Python packages used by the current tools include:

- `requests`
- `psutil`
- `pyttsx3`

Install the packages with:

```powershell
python -m pip install requests psutil pyttsx3
```

## API Token Setup

**An API token is required to run the AI-powered parts of this project.** An API token is a private credential that allows the application to authenticate with an AI service. Depending on the provider, API usage may have limits or incur costs.

### Which provider should you use?

The developer recommends obtaining your token from the **same AI provider that the project is configured to use**. This helps ensure that the token, account details, endpoint, and model are compatible. Using a token from an unrelated provider will not work unless the code is changed to support that provider.

If you are using the Cloudflare Workers AI configuration in the source code, create or access your Cloudflare account and obtain the required API credentials from Cloudflare's official dashboard. You may need both an account ID and an API token, depending on the configuration.

- Cloudflare dashboard: https://dash.cloudflare.com/
- Cloudflare Workers AI documentation: https://developers.cloudflare.com/workers-ai/

Always check the current source code to confirm which provider, model, endpoint, and credentials it expects.

### Configure your credentials

1. Identify the AI provider and the credential configuration used by the current version of the source code.
2. Create an API token with only the permissions required by the project.
3. Add your credentials locally using the configuration method expected by the code.
4. Keep real credentials private. **Never publish your token in this repository, README, screenshots, issues, or commit history.**
5. If a token has been exposed, revoke it and create a replacement immediately.

> **Security note:** If the current source code contains a token directly in a Python file, do not commit or push that file with a real token. Prefer environment variables or a local, untracked configuration file. Environment variables will only work automatically if the application code is written to read them.

## Installation and Running

1. Install Python and make sure `python` is available in PowerShell.
2. Download or clone this repository:

   ```powershell
   git clone https://github.com/sobhsafa31-afk/Kharazmi-agent.git
   cd Kharazmi-agent
   ```

3. Install the Python packages listed in the Requirements section.
4. Configure the required AI credentials as described above.
5. Locate the project's main Python entry-point file and run it. For example, if the entry point is named `main.py`:

   ```powershell
   python main.py
   ```

   Use the actual entry-point filename if it differs.

## Safety and Limitations

Kharazmi Agent can perform local actions, including creating and deleting files, depending on the enabled tools. Review requested paths and actions carefully before allowing the agent to execute them. Test with non-important files first, and avoid running the application with elevated privileges unless necessary.

This release reflects the project's `v0.1` codebase. AI-generated actions can be incorrect, so review important operations before execution. Future changes should be documented in subsequent releases.

## Project Structure

The repository currently includes these files:

- `Function.py` — local tool functions for file operations, application launching, and basic system information.
- `data_base.py` — SQLite-based storage for recent messages and long-term memory.
- `system_prompet.txt` — system instructions that guide the model's structured action responses.
- `README.md` — project overview and setup instructions.

The main application entry point and any additional files may vary as development continues.

## Contributing and Feedback

Suggestions, bug reports, and improvements are welcome. When reporting an issue, include the relevant error message and steps to reproduce it, but **never include API tokens, passwords, or other secrets**.

## Versioning

This project uses version tags and GitHub Releases to identify stable snapshots of the codebase. The current version is `v0.1`. Future releases should include a version tag, a summary of changes, and relevant setup notes.

## License

No license is specified in this repository yet. Until a license is added, do not assume that the project is available for unrestricted reuse, redistribution, or modification.
