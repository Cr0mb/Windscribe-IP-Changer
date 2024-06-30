# Windscribe-IP-Changer
The Windscribe IP Changer is a Python script designed to automate IP address changes using Windscribe VPN. 
With a user-friendly command-line interface (CLI), it provides flexibility in selecting server locations and setting change intervals, ensuring seamless operation and real-time status updates.

## Key Features
- Automated IP Address Rotation
- Real-time Status Updates (connection status and error messages)

## Prerequisites

- Windscribe CLI installed on your system
- Python 3.x
```
pip install colorama pyfiglet
```

> Ensure Windscribe CLI is installed and available in your PATH. Set the WINDSCRIBE_PATH environment variable if Windscribe is installed in a non-default location.

## Usage
```
Command-Line Interface
You can run the script with optional arguments for automation:

--location: Specify the server location (e.g., US, CA).
--interval: Specify the change interval in minutes.
```

**Adding CLI to PATH**

Unsure what to do on linux, but for windows you can right click on the windscribe app and click "Open File Location".

This will send you to windscribe's program files.

Look and make sure you have "windscribe-cli.exe" in this folder.

![image](https://github.com/Cr0mb/Windscribe-IP-Changer/assets/137664526/7a0f97c4-b216-4745-89c0-de9d71e4c008)

Now that you know the location of windscribe-cli, we need to add it to PATH.

You can do this by pressing the windows key and searching, "Environmental Variables". Here, you want to click" Environmental Variables," in the bottom right.

The page will look something like this:

![image](https://github.com/Cr0mb/Windscribe-IP-Changer/assets/137664526/af7e1a6f-d5e6-4be0-9936-1b0fd7142673)

Once in here, you want to pay attention to the second box, "System Variables," and double-click "Path"

![image](https://github.com/Cr0mb/Windscribe-IP-Changer/assets/137664526/f84c8edb-4529-42f8-b0bf-305742b4b1c5)

Next, you want to press, "New," and copy and paste the directory file of "windscribe-cli.exe" into PATH.





