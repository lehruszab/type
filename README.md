# Telegram Typing

A small Telegram userbot that simulates typing by progressively editing messages.

## Features

* `.type <text>` command
* Typing animation
* FloodWait handling
* `.env` configuration
* macOS launch script

## Requirements

* macOS
* Python 3.13+
* Telegram API credentials

## Setup

```bash
git clone <repository-url>
cd type
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create `.env`:

```env
API_ID=your_api_id
API_HASH=your_api_hash
```

Get Telegram API credentials from https://my.telegram.org/apps

## Run

```bash
python -m app.main
```

Or double-click:

```text
scripts/launch.command
```

## Usage

```text
.type Hello world
```

## Project

This project is continuously evolving.

The previous version contained the entire application in a single `main.py` file. The current version uses a modular structure with separate configuration, Telegram client, and typing engine.

## Security

Never commit:

```text
.env
*.session
*.session-journal
.venv/
```

## License

MIT
