from flask import Flask, render_template, make_response, jsonify, request, session, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route("/")
def index():  # TODO: show which songs are selected if collection exists in session
    songs_to_list = data_manager.get_songs_with_slides()
    root_url = request.url_root
    return render_template("index.html", list_of_songs=songs_to_list, root_url=root_url)


@app.route("/api/song-details/<song_id>")
def get_song_details(song_id):
    song_details = data_manager.get_song_details(song_id)
    return jsonify(**song_details)


@app.route("/api/collection/add-song", methods=["POST"])
def add_song_to_collection():
    new_song_data = request.form.to_dict()
    if "collection" not in session:
        session["collection"] = [new_song_data]
    else:
        session["collection"].append(new_song_data)
    session.modified = True
    return make_response("Choice has been saved", 200)


@app.route("/clear-collection", methods=["POST"])
def clear_collection():
    if "collection" in session:
        session.pop("collection")
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = "Mr. Slade Wilson"
    app.run(
        host="0.0.0.0",
        port=4321,
        debug=True
    )
