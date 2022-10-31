from flask import Flask, redirect, render_template, request, url_for
import dbContext as db

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/")
def home():
    dbContent = db.webContent()
    forward_message = ""
    return render_template('index.html', content = dbContent, forward_message=forward_message)

# @app.route("/sendMessage", methods=['POST'])
# def sendMessage():
#     if request.method == "POST":
#         senderName = request.form.get("senderName")
#         senderMail = request.form.get("senderMail")
#         senderSubject = request.form.get("senderSubject")
#         senderMessage = request.form.get("senderMessage")

#         dbContent = db.webContent()
#         dbContent.sendMessage(senderName, senderMail, senderSubject, senderMessage)
#         forward_message = "message has been sent..."
#         return render_template('index.html', content = dbContent, forward_message=forward_message)
#     else:
#         dbContent = db.webContent()
#         forward_message = "something went wrong..."
#         return render_template('index.html', content = dbContent, forward_message=forward_message)

if __name__ == "__main__":
    app.run()