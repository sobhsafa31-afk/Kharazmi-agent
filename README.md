# Kharazmi Agent

**A Python desktop assistant for Windows, powered by an LLM.**

Kharazmi Agent connects a language model to local tools so you can ask for supported file-system and system-information tasks in natural language. The **v0.2 release** introduces the project's web-search capability.

- **Latest release:** [Kharazmi Agent v0.2](https://github.com/sobhsafa31-afk/Kharazmi-agent/releases/tag/v0.2)
- **All releases:** [GitHub Releases](https://github.com/sobhsafa31-afk/Kharazmi-agent/releases)
- **Repository:** [sobhsafa31-afk/Kharazmi-agent](https://github.com/sobhsafa31-afk/Kharazmi-agent)

## Features

Depending on the selected release and its configuration, Kharazmi Agent supports:

- Conversational responses from a configured language model.
- Listing files and searching for files in a chosen directory.
- Creating folders and text files, and reading or deleting files.
- Opening supported folders and applications.
- Reporting RAM and disk-usage information.
- Storing recent conversation messages in a local SQLite database.
- Text-to-speech output where supported by the current version.
- Web search in the v0.2 release.

The exact actions available are determined by the files included in the release you run.

## Requirements

- Windows is recommended; some operations use Windows-specific features.
- Python 3.10 or later is recommended.
- An internet connection for the configured AI service and web-search functionality.
- An account and API credentials for the AI provider configured in the source.
- The Python packages listed in [requirements.txt](requirements.txt).

Install the dependencies from the repository folder:

```powershell
python -m pip install -r requirements.txt
```

## Download and run

1. Open the [v0.2 release page](https://github.com/sobhsafa31-afk/Kharazmi-agent/releases/tag/v0.2).
2. Download the files provided under **Assets**. Keep the files together in one folder, including the system prompt and database file when they are included in the release.
3. Install Python and the required packages as described above.
4. Open the configuration section in the relevant Python entry-point file and provide your own AI-provider account ID and API token if the version requires them.
5. From PowerShell, change to the folder containing the project files and run the entry-point file included in that release. For example:

   ```powershell
   python main.py
   ```

   If the downloaded version uses a different entry-point filename, run that file instead.

> **Important:** The repository's default branch and the files attached to a GitHub Release may not always be identical. For v0.2, use the files attached to the [v0.2 release](https://github.com/sobhsafa31-afk/Kharazmi-agent/releases/tag/v0.2) and follow the instructions for those files.

## AI provider configuration

The current source has been configured for Cloudflare Workers AI with the `@cf/meta/llama-3.1-8b-instruct` model. Confirm the endpoint, model, and required credentials in the exact release files you download, as these can change between versions.

- [Cloudflare Dashboard](https://dash.cloudflare.com/)
- [Cloudflare Workers AI documentation](https://developers.cloudflare.com/workers-ai/)

Never publish a real API token, account secret, password, or other credential in the repository, README, screenshots, issues, or commit history. Keep credentials private and use only the permissions required by the application. If a credential is exposed, revoke it and replace it.

## Local data and safety

- Conversation history and memory may be stored in a local SQLite database such as `memory.db`.
- Some tools can create, overwrite, read, or delete files. Review the requested path and action before allowing the agent to proceed.
- Test file operations on non-important sample files first.
- Do not run the application with administrator privileges unless that is necessary.
- AI-generated actions can be inaccurate. Verify important operations yourself.

## Project files

Files in the repository may include:

- `ui.py` or `main.py` — application interface and entry point, depending on the version.
- `Function.py` — local tool functions.
- `data_base.py` — SQLite conversation storage.
- `system_prompet.txt` — system instructions supplied to the model.
- `memory.db` — local database file, when included.
- `requirements.txt` — Python dependencies.

## Troubleshooting

- **Authentication/API errors:** Check your provider account, credentials, model name, endpoint, and any usage limits.
- **Missing Python modules:** Run `python -m pip install -r requirements.txt` from the project folder.
- **A feature is unavailable:** Confirm that you are running the files from the intended release and that its configuration is complete.
- **File-operation errors:** Check that the path exists and that your Windows account has the required permissions.

When asking for help, share the error message and steps to reproduce the problem, but remove API tokens, passwords, personal files, and other sensitive information first.

## Contributing and feedback

Bug reports, suggestions, and improvements are welcome. Please include concise reproduction steps and relevant error messages. Never include secrets or private data.

## Versioning

Releases are published on the [GitHub Releases page](https://github.com/sobhsafa31-afk/Kharazmi-agent/releases). Release notes should describe user-visible changes, setup requirements, and known limitations. Use the version's attached files as the source of truth for that release.

## License

No license is currently specified. Unless a license is added, do not assume that the project is available for unrestricted reuse, redistribution, or modification.
