from flask import Flask, render_template, request, session
from chatbot import get_answer


app = Flask(__name__)

app.secret_key = "chatbot_secret_key"



@app.route("/", methods=["GET", "POST"])
def home():

    if "messages" not in session:
        session["messages"] = [
            {
                "type": "bot",
                "text": "Hi 👋 I am your Laptop Assistant. How can I help you?"
            }
        ]


    if request.method == "POST":

        question = request.form["question"]

        answer = get_answer(question)


        session["messages"].append(
            {
                "type": "user",
                "text": question
            }
        )


        session["messages"].append(
            {
                "type": "bot",
                "text": answer
            }
        )


        session.modified = True



    return render_template(
        "index.html",
        messages=session["messages"]
    )




@app.route("/clear")
def clear():

    session.clear()

    return home()




if __name__ == "__main__":

    app.run(debug=True)