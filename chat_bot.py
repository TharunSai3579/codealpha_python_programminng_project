from nltk.chat.util import Chat,reflections
pairs=[
    [r"hi",["hello how can i help you"]],
    [r"tell me about yourself",["I am chatbot i can help you virtually by providing you what you want"]],
    [r"who created you",[" Tharun Sai Ramireddy  created me "]],
    [r"what is your age",[" im just young like you"]],
    [r"how are you",["i am good and doing well and hoping the same for you"]],
    [r"where are you from",["i wasn't borned i was created"]],
    [r"i am not felling well",["dont worry everything will be alright"]],
    [r"what language do you speak",[" i speak english"]],
    [r"are you an ai",[" i am chatbot i will help you through text"]],
    [r"can you finish my work",[" i can help you by providing answers to it"]]
]
chat=Chat(pairs,reflections)
chat.converse()
def quit():
    print("hey i am chat bot how cam i assist... ")
if __name__=="__main__":
    quit()
    

