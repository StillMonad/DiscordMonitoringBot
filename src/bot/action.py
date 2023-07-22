from datetime import datetime


class Action:
    def __init__(self, name, guild, channel, action, message=""):
        self.time = datetime.now()
        self.name = name
        self.guild = guild
        self.channel = channel
        self.action = action
        self.message = message

    def __repr__(self):
        return (
            "[created='%s'] guild='%s', channel='%s', name='%s', action='%s', message='%s'"
            % (
                self.time,
                self.guild,
                self.channel,
                self.name,
                self.action,
                self.message,
            )
        )

    def verbose(self):
        name = self.name[0 : self.name.find("#")]
        if self.action in ['joined', 'left']:
            return f"{self.name} {self.action} channel {self.channel} in {self.guild}"
        elif self.action in ['message']:
            return f"{self.name} sent message in channel {self.channel} in {self.guild}: {self.message}"
        else:
            return f"{self.name} {self.action}"
