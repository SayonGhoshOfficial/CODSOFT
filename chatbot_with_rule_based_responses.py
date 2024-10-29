import random
import re


class SupportBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'taste_reviews': r'.*\s*taste.*reviews.*',
            'about_returns': r'.*\s*return.*policy.*',
            'general_query': r'.*how.*help.*'
        }

    def greet(self):
        self.name = input('Hey! May I know  your name?\n')
        will_help = input(f'{self.name} Do you want to ask something? I shall be grateful to assist you \n')
        if will_help in self.exit_commands:
            print("Alright ! See you tomorrow\n")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Alright ! see you soon\n")
                return True
            return False

    def chat(self):
        reply = input("please tell me your query\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == "ask_about_product":
                return self.ask_about_product()
            elif found_match and intent == "taste_reviews":
                return self.taste_reviews()
            elif found_match and intent == "about_returns":
                return self.about_returns()
            elif found_match and intent == "general_query":
                return self.general_query()
        return self.no_intent_matched()

    def ask_about_product(self):
        responses = ("Our produce is of high-quality ingredients and hygienically prepared\n",
                     "Our milk products are full of vitamins and minerals\n")
        return random.choice(responses)

    def taste_reviews(self):
        responses = "Our produce taste amazing and fresh prepared from fresh milk\n"
        return random.choice(responses)

    def about_returns(self):
        responses = ("Open sealed products cannot be returned\n",
                     "If seal is broken or pack is tampered it cannot be returned\n")
        return random.choice(responses)

    def general_query(self):
        responses = ("How can I assist you further?\n",
                     "Is there anything I can help you with?\n")
        return random.choice(responses)

    def no_intent_matched(self):
        responses = ("You may seek further information from our website\n",
                        )
        return random.choice(responses)


bot = SupportBot()
bot.greet()