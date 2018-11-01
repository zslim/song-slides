from flask import Flask, render_template, make_response, jsonify, request, session, redirect, url_for, send_file
import data_manager
import utils
import file_handler

app = Flask(__name__)


@app.route("/")
def index():
    songs_to_list = data_manager.get_songs_with_slides()
    list_of_places = data_manager.get_song_places()
    root_url = request.url_root
    return render_template("index.html", list_of_songs=songs_to_list, list_of_places=list_of_places, root_url=root_url)


@app.route("/api/song-details/<song_id>")
def get_song_details(song_id):
    song_details = data_manager.get_song_lyrics(song_id)
    song_details["index_data"] = data_manager.get_song_index_details(song_id)
    return jsonify(**song_details)


@app.route("/api/song-index-data/<song_id>")
def get_song_index_details(song_id):
    index_data = data_manager.get_song_index_details(song_id)
    return jsonify(index_data)


@app.route("/api/collection/add-song", methods=["POST"])
def add_song_to_collection():
    new_song_data = request.form.to_dict()
    if "collection" not in session:
        session["collection"] = [new_song_data]
    elif new_song_data["place"] == "Áldozás":
        session["collection"].append(new_song_data)
    else:
        # TODO: if a song gets implicitly deleted because another song is selected on its place, it should be deleted from the collection pane & original button should be set on song browser pane
        session["collection"][:] = [song for song in session["collection"] if song["id"] != new_song_data["id"] and song["placeId"] != new_song_data["placeId"]]
        session["collection"].append(new_song_data)
    session.modified = True
    index_data_for_song = data_manager.get_song_index_details(new_song_data["id"])
    return jsonify(index_data_for_song)


@app.route("/api/collection/remove-song", methods=["POST"])
def remove_song_from_collection():
    song_id = request.form["id"]
    session["collection"][:] = [song for song in session["collection"] if song["id"] != song_id]
    session.modified = True
    return make_response("Song cleared from collection", 200)


@app.route("/clear-collection", methods=["POST"])
def clear_collection():
    if "collection" in session:
        session.pop("collection")
    return redirect(url_for("index"))


@app.route("/api/download-slides")
def download_slides():
    if "collection" not in session:
        return make_response("No song selected", 404)
    else:
        ordered_collection = utils.sort_list_of_dicts(session["collection"], "placeId")
        tuple_of_song_ids = utils.get_values_of_identical_keys(ordered_collection, "id")
        slide_paths = data_manager.get_slide_paths_by_song_id(tuple_of_song_ids)
        path_of_zipfile = file_handler.zip_slides(slide_paths)
        file_name = file_handler.create_downloading_name()
        return send_file(path_of_zipfile, as_attachment=True, attachment_filename=file_name)


if __name__ == '__main__':
    app.secret_key = "Mr. Slade Wilson"
    app.run(
        host="0.0.0.0",
        port=4321,
        debug=True
    )
