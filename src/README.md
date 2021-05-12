# friend_bot

Friend bot is a discord bot that simulates your friends using a JSON file of quotes.

## Usage ##

1. Register a bot account with Discord - see [this guide](https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro) for how to do that.
1. Clone this repo.
1. (Recommended) Create and source a virtual environment: `pyhton3 -m venv .venv; source .venv/bin/activate`.
1. Run `pip install -r requirements.txt` in the root directory of this repo.
1. Create a JSON file populated with your chosen quotes (example below).
1. Create an appropriate `.env` file (example below).

## JSON Datafile Example ##

```
{
    [
        "first quote",
        "second quote",
        "third quote"
    ]
}
```

## .env File Example ##

```
API_KEY=[Your bot's token]
DATA_FILE=[path to your json file]
```