from flask import Flask, render_template
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    songs_to_list = data_manager.get_songs_with_slides()
    return render_template("index.html", list_of_songs=songs_to_list)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=4321,
        debug=True
    )
