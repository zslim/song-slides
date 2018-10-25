from flask import Flask, render_template, make_response, jsonify
import data_manager

app = Flask(__name__)


@app.route("/")
def index():
    songs_to_list = data_manager.get_songs_with_slides()
    return render_template("index.html", list_of_songs=songs_to_list)


@app.route("/api/song-details/<song_id>")
def get_song_details(song_id):
    song_details = data_manager.get_song_details(song_id)
    return jsonify(**song_details)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=4321,
        debug=True
    )
