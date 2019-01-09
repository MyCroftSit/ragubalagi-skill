from mycroft import MycroftSkill, intent_file_handler


class Ragubalagi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ragubalagi.intent')
    def handle_ragubalagi(self, message):
        self.speak_dialog('ragubalagi')


def create_skill():
    return Ragubalagi()

