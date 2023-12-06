# Setup a Telegram bot that stores data to Google Spreadsheets using Apps Scripts

## Problem solving

* (Part 1) Allow a Google Spreadsheet sheet to recieve POST requests with data and store it into the next empty row
* (Part 2) Create a Telegram bot and store its credentials
* (Part 3) Create a Google Cloud function that listens Telegram webhook
* (Part 4) Set up the Telegram bot to point it to the Google Cloud

## Part 1 -- Allow a Google Spreadsheet sheet to recieve POST requests with data and store it into the next empty row

1. Create a new Google Spreadsheets document.
2. Add a new sheet named `data` (or rename `Sheet1` to `data`)
6. Now copy the URL and replace the `GOOGLE_SCRIPTS_URL` in the `main.py` file.
3. In the cell `A1` type `A`, in `B1`->`B`, `C1`->`C`, `D1`->`D`
4. Click `Extensions>Apps Scripts` and paste the content of `google-scripts.js` in it.
5. Click `publish`, select `web application` and accept all unsecure stuff in the following dialogs.
6. At the end a URL like this will be provided `https://script.google.com/macros/s/iausudhliaushfiuasdhfliuhdslifuhIU76T7AS6FYGYA7SD/exec`
7. Now copy the URL and replace the `GOOGLE_SCRIPTS_URL` in the `main.py` file.

## Part 2 -- Create a Telegram bot and store its credentials

1. Start a chat with `@Botfather`. You can follow this link and it will open on your browser or Telegram Desktop. [https://telegram.me/BotFather](https://telegram.me/BotFather).

2. Type `/newbot` to create a new bot.
    * Response: `Alright, a new bot. How are we going to call it? Please choose a name for your bot.` (How it will appear on the lists, not the username)

3. Set the name of the bot. For example `My first bot`
    * Response: `Good. Now let's choose a username for your bot. It must end in 'bot'. Like this, for example: TetrisBot or tetris_bot.` Take into account that there are a lot of "taken" usernames so it may be difficult to find an empty one.

4. Type the username for the bot. I used `aoisudha9_bot`.
    * Response: `Done! Congratulations on your new bot. You will find it at t.me/aoisudha9_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.`

    * And the most important part, it returns you the bot token, the way to authenticate after that you are the bot owner. `Use this token to access the HTTP API: mysupertoken980987987098:98u9879879879 Keep your token secure and store it safely, it can be used by anyone to control your bot.`

5. Copy the token to a notepad and keep it for later.

## Part 3 -- Create a Google Cloud function that listens Telegram webhook

0. Go through the full quickstart tutorial. [Here](https://cloud.google.com/sdk/docs/install-sdk)
    * Now you should have a project, the CLI installed on the computer and authenticated. Ready to start executing commands such as `gcloud auth list`.

1. [Enable Gcloud Functions API](https://console.cloud.google.com/marketplace/product/google/cloudfunctions.googleapis.com)

2. Create a Google Cloud Function running this command in the same line:

```bash
gcloud functions deploy telegram_bot --set-env-vars "TELEGRAM_TOKEN=<TELEGRAM_TOKEN>" --runtime python38 --trigger-http --project=<GCLOUD-PROJECT>
```

* `telegram_bot` the name of the function we want to execute in the `main.py` file.
* `<TELEGRAM_TOKEN>` the Telegram token copied before. This will be used to authorise the Cloud Function against Telegram API.
* `<GCLOUD-PROJECT>` Your recently created `Project ID`. Example: `my-project-1234`
* `--runtime python38` describe the environment used by our function, Python 3.8 in this case
* `--trigger-http` is the type of trigger associated to this function.

You can also specify the region by appending the following string to the previous command. [List of the available regions](https://cloud.google.com/compute/docs/regions-zones)

```bash
--region=<region_name>
```

If everyting was ok, this message should appear before listing all Function details:
`...done.`

## Part 4 -- Set up the Telegram bot to point it to the Google Cloud

Now we need to indicate Telegram to send a request to our Google Cloud Function each time a user sends a message to our bot. First we will find the trigger url and then send it to Telegram.

### Finding the function URL-trigger

* You can find your function listed in the [GCloud Functions List](https://console.cloud.google.com/functions/list)
* Then, depending on the generation of the function you can do:
  * 1st gen: `gcloud functions describe <YOUR_FUNCTION_NAME> --format="value(httpsTrigger.url)"`
  * 2nd gen `gcloud functions describe <YOUR_FUNCTION_NAME> --gen2 --region=<YOUR_FUNCTION_REGION> --format="value(serviceConfig.uri)"`

* In our case the name is `telegram_bot`, so the full command to retrieve the trigger url will be `gcloud functions describe telegram_bot --format="value(httpsTrigger.url)"`

### Submiting the URL to Telegram

We can do so using this request to the API:

```bash
curl "https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook?url=<URL>&drop_pending_updates=true"
```

* `<TELEGRAM_TOKEN>` the previously copied token, note the preppend of the `bot` string.
* `<URL>` the url where te Cloud Function listens.

Once this success message should be returned:
`{"ok":true,"result":true,"description":"Webhook was set"}`




https://api.telegram.org/bot5785288507:AAEZAqEoukhirWfn_Aa0ohj3AtAiRx5rMN4/getUpdates
