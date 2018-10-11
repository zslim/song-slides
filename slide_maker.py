import PIL
from PIL import Image, ImageDraw, ImageFont
import data_manager


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
    songs_to_slidify = data_manager.get_songs_with_no_slide()

    slide_info_csv = "data/slides.csv"
    slide_info = csv_handler.read_csv(slide_info_csv)

    for dict_of_song in songs_to_slidify:
        slides_of_song = [row for row in slide_info if row["song_id"] == dict_of_song["id"]]

        for i in range(len(slides_of_song)):
            first_line_current = slides_of_song[i][""]
            text_of_slide = dict_of_song["lyrics"].splitlines()[]
            pass


if __name__ == '__main__':
    lyrics = "1st row with exactly 40 characters here\n2nd row with exactly 40 characters here\n3rd row with exactly 40 characters here\n4th row with exactly 40 characters here\n5th row with exactly 40 characters here\n6th row with exactly 40 characters here\n7th row with exactly 40 characters here\n8th row with exactly 40 characters here\n9th row with exactly 40 characters here\n10th row with exactly 41 characters here\n"
    img_size = (720, 520)
    font_size = 38
    img_path = "static/images/trial/trial5.png"

    draw_slide(lyrics, img_size, font_size, img_path)
