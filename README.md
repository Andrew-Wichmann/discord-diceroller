# imperial-dicebot
A Discord.py die rolling bot for Imperial Dawn, an excellent tabletop RPG

The game itself is available for free at https://imperialdawn.com

This uses the discord.py library available at https://github.com/Rapptz/discord.py, which is pretty great all things considered, especially for setting up simple bots.

When making a discord bot, be sure that you are trying to log in with your bot's token, not their Client ID or Client secret. You can do so with this code by creating a text file called "token" (not "token.txt", "token.docx", or "token.pdf", just "token") in the same directory as the code, and pasting your token into it without leaving anything in the file.

While not super satisfying to use, the dicebot.sh script will restart your bot after it crashes periodically. This is pragmatic, as errors that I don't yet understand seem to come through sometimes, especially when working over a spotty connection. If not caught, they can crash the entire bot, which is annoying.

This code should be considered free to use or learn from by anyone, attribution is preferred if appropriate but not required. There's probably an official license that says that, but I don't feel like digging through contracts right now, and realistically nobody's gonna rip off a bot this simple. I probably wouldn't even care if they did.

I'd love to hear any suggestions for usability or reliability improvements, please feel free to leave a comment, issue, etc.
