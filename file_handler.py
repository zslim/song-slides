import os, os.path
import zipfile


def create_temporary_filename(directory_path, extension, with_path=True):
    list_of_files_in_directory = [name for name in os.listdir(directory_path)
                                  if os.path.isfile(os.path.join(directory_path, name))]
    file_number = len(list_of_files_in_directory) + 1
    file_name = f"tempfile_{file_number:03}.{extension}"

    if with_path:
        return os.path.join(directory_path, file_name)
    else:
        return file_name


def zip_slides(list_of_slide_paths):
    directory_of_zips = "sending"
    file_extension = "zip"
    path_of_zipfile = create_temporary_filename(directory_of_zips, file_extension)

    with zipfile.ZipFile(path_of_zipfile, "w") as temporary_zip:
        for (index, path) in enumerate(list_of_slide_paths):
            name_in_zip = f"alma{index + 1:04}.jpg"
            temporary_zip.write(path, arcname=name_in_zip)

    return path_of_zipfile
