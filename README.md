Simple PHPSpec commands
===============
This plugin allows you the run the PHPSpec tests using the Sublime Text interface, without having to open and use the command line.

This package was originally intended for personal purposes. I forked the original SimplePHPunit package and renamed the functions to properly work with PHPSpec. I liked the idea of running the tests from inside Sublime, so this package was made. All credits and attribution goes to the original creator. You can view the original package on [GitHub](https://github.com/m0nah/SimplePHPUnit-for-Sublime-Text "Github").

### Available commands:

- `PHPSpec: Run`
- `PHPSpec: Run with params`

### Installation:
Via Package Control, search for `SimplePHPSpec`

### Usage:
Press ctrl + shift + p for the dropdown command list, search for `PHPSpec: `, and pick your command. Also you can use `Tools/PHPSpec...` menu item

### Keybinding:

You can use command `simple_phpspec` for your keybinding. Example:

Example:

```json
{ "keys": ["super+ctrl+alt+space"], "command": "simple_phpspec" }
```

### Notes:
- If you want the command to pick up your custom phpspec.yml configuration file, it needs to be in the root folder of your project in the sidebar.
- You need to insert in the Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.

### Donate:
If you liked this plugin, you can donate to the original author to support it!

[![Paypal donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SZ6YWJUGFM9J8)

Feedback and contributions are really appreciated.
