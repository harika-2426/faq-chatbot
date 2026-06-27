import json
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



with open("data/faq.json","r",encoding="utf-8") as file:
    faqs=json.load(file)



questions=[
    item["question"]
    for item in faqs
]



vectorizer=TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)


faq_vectors = vectorizer.fit_transform(
    questions
)





def get_answer(user_question):

    text=user_question.lower().strip()



    # Human conversation

    greetings=[
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good evening"
    ]


    if any(text == word for word in greetings):

        return random.choice([
            "Hello 👋 How can I help you today?",
            "Hi 😊 Feel free to ask me about the product.",
            "Hey! I am here to help you 🤖"
        ])




    if "how are you" in text:

        return "I'm doing great 😄 Thanks for asking!"



    if "your name" in text:

        return "I am your Product Assistant 🤖"
    
    if text in [
       "ok",
       "okay",
       "okayy",
       "alright",
       "fine"
    ]:

     return random.choice([
         "Great 😊 Let me know if you need anything else.",
         "Okay 👍 I'm here if you have more questions.",
         "Sure 😊 Feel free to ask me."
     ])


    if "thank" in text:

        return "You're welcome 😊 Let me know if you have more questions."



    if text in [
        "i have a doubt",
        "i have a question",
        "can you help me",
        "help"
    ]:

        return "Sure 😊 Ask me anything about the product. I will help you."





    # Product question matching

    user_vector = vectorizer.transform(
        [text]
    )


    similarity = cosine_similarity(
        user_vector,
        faq_vectors
    )


    index = similarity.argmax()


    score = similarity[0][index]




    # only answer if it is actually related

    if score >= 0.35:

        return faqs[index]["answer"]




    return (
        "I understand 😊 Could you please explain your question "
        "a little more? I can help with product details, features, "
        "warranty, performance and usage."
    )