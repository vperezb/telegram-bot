# Setup a Telegram bot that stores data to Google Spreadsheets using Apps Scripts

## Problem solving

* (Part 1) Create a Telegram bot and store its credentials
* (Part 2) Create a Google Cloud function that listens Telegram webhook
* (Part 3) Set up the Telegram bot to point it to the Google Cloud 
* (Part 4) Allow a Google Spreadsheet sheet to recieve POST requests with data and store it into the next empty row

## Part 1 -- Create a Telegram bot and store its credentials

1. Start a chat with `@Botfather`. You can follow this link and it will open on your browser or Telegram Desktop. [https://telegram.me/BotFather](https://telegram.me/BotFather).

2. Type `/newbot` to create a new bot.
    - Response: `Alright, a new bot. How are we going to call it? Please choose a name for your bot.` (How it will appear on the lists, not the username)

3. Set the name of the bot. For example `My first bot`
    - Response: `Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.` Take into account that there are a lot of "taken" usernames so it may be difficult to find an empty one.

4. Type the username for the bot. I used `aoisudha9_bot`.
    - Response: `Done! Congratulations on your new bot. You will find it at t.me/aoisudha9_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.`

    - And the most important part, it returns you the bot token, the way to authenticate after that you are the bot owner. `Use this token to access the HTTP API: mysupertoken980987987098:98u9879879879 Keep your token secure and store it safely, it can be used by anyone to control your bot.`

5. Copy the token to a notepad and keep it for later.

## Part 2 -- Create a Google Cloud function that listens Telegram webhook

This part 

Create a Google Cloud Function running this command in the same line:

```
gcloud functions deploy telegram_bot --set-env-vars "TELEGRAM_TOKEN=xxx" --runtime python38 --trigger-http --project=my-telegram-bot
```

You can also specify the region by appending the following string to the previous command. [List of the available regions](https://cloud.google.com/compute/docs/regions-zones)

```
--region=<region_name>
```

Some details:

* Here webhook is the name of the function in the `main.py` file
* You need to specify your Telegram token with the `--set-env-vars` option
* `--runtime python38` describe the environment used by our function, Python 3.8 in this case
* `--trigger-http` is the type of trigger associated to this function.

## Part 2
 
You need to set up your Webhook URL in "Telegram" using this API call:

```
curl "https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook?url=<URL>&drop_pending_updates=true"
```
