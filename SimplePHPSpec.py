import os
import sys
import shlex
import subprocess
import sublime
import sublime_plugin

if sys.version_info < (3, 3):
    raise RuntimeError('SimplePHPSpec works with Sublime Text 3 only')

SPU_THEME = 'Packages/SimplePHPSpec/SimplePHPSpec.hidden-tmTheme'
SPU_SYNTAX = 'Packages/SimplePHPSpec/SimplePHPSpec.hidden-tmLanguage'

class ShowInPanel:
    def __init__(self, window):
        self.window = window

    def display_results(self):
        self.panel = self.window.get_output_panel("exec")
        self.window.run_command("show_panel", {"panel": "output.exec"})

        self.panel.settings().set("color_scheme", SPU_THEME)
        self.panel.set_syntax_file(SPU_SYNTAX)

class SimplePhpSpecCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SimplePhpSpecCommand, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        try:
            # The first folder needs to be the Laravel Project
            settings = sublime.load_settings('SimplePHPSpec.sublime-settings')
            self.phpspec_path = settings.get('phpspec_path')
            self.PROJECT_PATH = self.window.folders()[0]
            self.params = kwargs.get('params', False)
            default_settings = ['run'] + settings.get('phpspec_default_args')
            default_settings = ['{0} '.format(elem) for elem in default_settings]
            self.args = [self.phpspec_path, default_settings]
            if self.params is True:
                self.window.show_input_panel('Params:', '', self.on_params, None, None)
            else:
                self.on_done()
        except IndexError:
            sublime.status_message("Cannot launch PHPSpec, please set the correct path in your preferences.")

    def on_params(self, command):
        self.command = command
        self.args.extend(shlex.split(str(self.command)))
        self.on_done()

    def on_done(self):
        if os.name != 'posix':
            self.args = subprocess.list2cmdline(self.args)
        try:
            self.run_shell_command(self.args, self.PROJECT_PATH)
        except IOError:
            sublime.status_message('IOError - command aborted')

    def run_shell_command(self, command, working_dir):
            self.window.run_command("exec", {
                "cmd": command,
                "shell": os.name == 'nt',
                "working_dir": working_dir
            })
            self.display_results()
            return True

    def display_results(self):
        display = ShowInPanel(self.window)
        display.display_results()

    def window(self):
        return self.view.window()
