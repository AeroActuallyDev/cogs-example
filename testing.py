#This file lets you test the bot the way it would recieve settings in docker env. if you know what i mean.

from os import environ

environ["SELFBOT"] = "name"
environ["VERSION"] = "1"
environ["BRANCH"] = "main"
environ["WHITELIST"] = "aero"
environ["REGION"] = "EU-UK"
environ["SERVER_IDENTIFIER"] = "Test123" 
environ["SERVER_ADMIN_KEY"] = "Test123"

environ["HTTP_SCHEME"] = "https"
environ["WEBSOCKET_SCHEME"] = "wss"
environ["MASTER_SERVER"] = "api.cogs.sbs"

import index
