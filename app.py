from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/messages', methods = ['POST'])
def api_message():
    f = open('./file.wav', 'wb')
    f.write(request.data)
    f.close()
    return "Binary message written!"



if __name__ == "__main__":
    app.run(debug=True)
