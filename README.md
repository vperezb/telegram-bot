# Setup a Telegram bot that stores data to Google Spreadsheets using Apps Scripts

## Problem solving

* (Part 1) Create a Telegram bot and store its credentials
* (Part 2) Create a Google Cloud function that listens Telegram webhook
* (Part 3) Set up the Telegram bot to point it to the Google Cloud 
* (Part 4) Allow a Google Spreadsheet sheet to recieve POST requests with data and store it into the next empty row

## Part 1 -- Create a Telegram bot and store its credentials

The first thing we need to do is to create the Telegram bot, it can be easily done by starting a chat with the "@Botfather". You can follow this link and it will open on your browser or Telegram Desktop. [https://telegram.me/BotFather](https://telegram.me/BotFather).

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
