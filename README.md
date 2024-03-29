# fail2telegram

fail2telegram is a simple action for the [fail2ban](https://github.com/fail2ban/fail2ban) project that can send telegram notifications whenever an IP gets banned/unbanned.

Easy to install and easy to use.

## Prerequisites

- python3+
- fail2ban installed on server

## Installation

### 1. Downloading

Use `git clone` to download the repository to your local machine / server:

```bash
> git clone https://github.com/Pyenb/fail2telegram
```

Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages from the `requirements.txt`.

```bash
> pip3 install -r requirements.txt
```

### 2. Moving the files

Move the files `telegram.py` and `telegram_config.json` into the `action.d` folder inside of your fail2ban installation location. (e.g. `/etc/fail2ban/action.d`)

###### Note: If your installation location differs from the default `/etc/fail2ban/action.d`, edit the `self.installpath` variable inside the `telegram.py`

### 3. Editing

Edit your `jail.local` config and add the line:

```
action = telegram.py
```

to your `# JAILS`. e.g:

```
#
# JAILS
#

[sshd]

enabled = true
action = telegram.py
maxretry = 5
findtime = 6h
bantime = 12h
port    = ssh
logpath = %(sshd_log)s
backend = %(sshd_backend)s
```

and save the changes of course.

### 4. Telegram Bot

Now we need to create a new telegram bot. For that open a new chat with [BotFather](https://telegram.me/botfather), type in the command `/newbot` and follow the instructions. In the end you should see a message like this:

![success](https://i.imgur.com/ugOzB1B.png)

Now copy the token to access the HTTP API and paste it into the `telegram_api_token` entry inside of the `telegram_config.json`. (Don't worry about the `telegram_chat_id`)

### 5. Chatting

Start a chat with your newly created bot and send a message (can be whatever).

### 6. Starting

Restart the fail2ban service using:

```bash
> service fail2ban restart
```

and check if the bot got the chat ID using:

```bash
> service fail2ban status
```

the expected output should look something like this:

![status](https://i.imgur.com/wArFf0Q.png)

If everything is working, you should start getting telegram notifications whenever someone gets banned or unbanned.

![texts](https://i.imgur.com/GcAVd5R.png)

###### Note: will send everyone that got banned/unbanned in the timeframe defined by `findtime` at startup. After that just new stuff.

## Usage

The telegram bot will send you everything automatically. But if you only want to receive a message when an IP gets banned or unbanned (not both), edit the `telegram_config.json` again and set the variables `receive_banned` and `receive_unbanned` to `false`. Only the variables set to `true` will be send as a telegram notification. e.g:

![config](https://i.imgur.com/OjWNHwl.png)

After that just execute to reload fail2ban and load the new configuration.

```bash
> service fail2ban restart
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Disclaimer
This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.
