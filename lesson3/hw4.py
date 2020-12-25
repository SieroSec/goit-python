import os, sys

if len(sys.argv) >= 2:
   path = sys.argv[1]
else:
   path = "C:\\projects\\goit-python\\lesson3\\mess"
print(f"Start in {path}")

files = os.listdir(path)

photo_ext = ["jpg", "png", "jpeg", "gif"]
video_ext = ["mov","mpeg","mp4","avi"]
music_ext = ["mp3","ogg","wav","amr"]
document_ext = ["txt","doc","docx","pdf"]
found_ext = set()

# found filenames are put in these lists
photos = []
videos = []
music = []
documents = []
unknown_files = []

for file in files:
   file_extension = (file[file.index("."):])[1:] # [1:] - removes dot
   print(file_extension)
   # create a set with all extensions of the files in the folder
   found_ext.add(file_extension)

   if file_extension in photo_ext:
      photos.append(file)
   elif file_extension in video_ext:
      videos.append(file)
   elif file_extension in music_ext:
      music.append(file)
   elif file_extension in document_ext:
      documents.append(file)
   else:
      found_ext.add(file_extension)
      unknown_files.append(file)

print(f"photos: {photos}\n\n videos: {videos}\n\n music files: {music}\n\n documents: {documents}\n\n other: {unknown_files}\n\n Found extentions: {found_ext}")