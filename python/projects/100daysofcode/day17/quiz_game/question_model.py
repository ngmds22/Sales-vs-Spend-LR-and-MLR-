class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
    def display_question(self):
        return self.prompt
    
    def check_answer(self, user_answer):
        return self.answer == user_answer