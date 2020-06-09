from mycroft import MycroftSkill, intent_file_handler


class CitiBike(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bike.citi.intent')
    def handle_bike_citi(self, message):
        self.speak_dialog('bike.citi')


def create_skill():
    return CitiBike()

