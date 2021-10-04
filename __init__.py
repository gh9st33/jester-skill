from mycroft import MycroftSkill, intent_file_handler


class Jester(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jester.intent')
    def handle_jester(self, message):
        self.speak_dialog('jester')


def create_skill():
    return Jester()

