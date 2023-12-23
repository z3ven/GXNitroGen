
<div align="center">
  <h1>GXNitroGen</h1>
  <p>Generate free discord nitro using OperaGX giveaway</p>
  <img src="asset.png">

  
  <a href="">Warning</a>
  <a href="">Installation</a>
  <a href="">Usage</a>
  <a href="">Issues</a>
  <a href="">Notice</a>
  <a href="">Contribution</a>
</div>


# Warning

Please read this section carefully before you use the GXNitroGen tool.
- It expires on June 17th, 2024 (11:59PM PST), because its the official end of the giveaway
- This tool is provided as-is without any warranties. You can use it at your own risk.
- Contributors are not responsible for any misuse of this tool.
# Installation

To install GXNitroGen, follow these steps:

1. Clone the repository using the following command:

    ```bash
    git clone https://github.com/z3ven/GXNitroGen/
    ```

2. Navigate to the 'GXNitroGen' directory:

    ```bash
    cd GXNitroGen-main
    ```

3. Install the required dependencies using:

    ```bash
    pip3 install -r requirements.txt
    ```

# Usage

To use GXNitroGen, follow these steps:
## Creating Discord bo
Create a discord bot in the Discord Developer Portal and obtain the token and client ID.
## Editing config
Now you should edit the `config.json` file. Open it in your favorite code editor.
## Token and Client ID
Now when you obtained the token and client ID paste them into the `token` and `client_id`
Your config file will look like this:
## Proxies
Your request might be blocked by Opera's servers, so you should use proxies
1. Find a proxy server. It can be free or paid. NOTE! Free proxies are dying fast!
2. Then paste this to the `proxy` dictionary
   ```json
   "https": "https://example_proxy.org:123456",
   "http": "http://another_proxy.org:7890"
   ```
   Each line represents the proxy server.
   The key is the protocol that the proxy server uses. It can be both http and https. 
   The value is separated into 2 parts
   The first part is a URL(which is before `:`)
   And port(which is after `:`)
   Remember to correct all the stuff in the proxy
## Addinotal config editing
You can also edit activity text by setting it in `activity_message`
And you can edit help_message by setting it in `help_message`

# Issues
## `discord.errors.LoginFailure: Improper token has been passed.`
This error is displayed in the terminal. It means that you entered an improper token. Correct it in `config.json`
## `Unknown application`
This is in the browser. You entered the wrong client id.
## `nodename nor servname provided, or not known`
Sadly, your proxy died, or you entered method or URL incorrectly

# Notices

Please note the following:

- Run it using python3. python2 will not work
- Your requests might be blocked, so use a proxy server
- Do not make your bot public, unless you don't want to get banned

# Contributing

If you would like to contribute to GXNitroGen, please follow these guidelines:

1. Fork the repository and create a new branch.
2. Make your changes and test thoroughly.
3. Create a pull request with a clear description of your changes.

Your contributions are highly appreciated!

