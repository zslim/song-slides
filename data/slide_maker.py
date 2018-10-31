from PIL import Image, ImageDraw, ImageFont
import data_manager
from data import csv_handler
import utils


def draw_slide(text, slide_size, size_of_font, path_to_save, path_to_font=None):
    text_color = "white"
    text_starting_position = (20, 30)

    font_name = "arial.ttf"
    if path_to_font:
        font_name = path_to_font

    draw_font = ImageFont.truetype(font_name, size_of_font)
    new_image = Image.new("L", slide_size)
    draw = ImageDraw.Draw(new_image)

    draw.text(text_starting_position, text, text_color, draw_font)
    new_image.save(path_to_save)


def create_new_slides():
    songs_to_slidify = data_manager.get_songs_without_slides()

    slide_info_csv = "data/slides.csv"
    slide_info = csv_handler.read_csv(slide_info_csv)

    slide_arguments = {"slide_size": (720, 520), "size_of_font": 38}

    for dict_of_song in songs_to_slidify:
        slides_of_song = [row for row in slide_info if row["song_id"] == dict_of_song["id"]]

        for i in range(len(slides_of_song)):
            current_slide = slides_of_song[i]
            first_line = current_slide["slide_first"] - 1
            last_line = current_slide["slide_last"]
            text_of_slide = "\n".join(dict_of_song["lyrics"].splitlines()[first_line:last_line])
            fancy_text = utils.strip_newlines_from_edges(text_of_slide)

            path_of_slide = f"static/images/slides/song_{dict_of_song['id']}_slide_{current_slide['slide_number']}.png"
            draw_slide(fancy_text, path_to_save=path_of_slide, **slide_arguments)
            # TODO: check if png is compatible with the projector
            slide_data = {"song_id": current_slide["song_id"],
                          "slide_number": current_slide["slide_number"],
                          "path": path_of_slide}
            data_manager.save_new_slide(slide_data)


if __name__ == '__main__':
    create_new_slides()
