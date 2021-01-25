from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = "Quiz app"
    name = "index"
    return render_template(
        'index.html', 
        title = title,
        name = name
    )

@app.route('/games')
def games():
    title = "Lista quizów"
    name = "games"
    return render_template(
        'games.html',
        title = title,
        name = name
    )