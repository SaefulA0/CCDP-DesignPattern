# command_invoker.py

class CommandInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run_commands(self):
        for command in self.commands:
            command.execute()
