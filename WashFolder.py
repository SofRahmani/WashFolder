import glob
import shutil
import os
from os import path

# ? Tri les fichiers d'un dossier par type
extensionsVideos    = ['.avi', '.tvs', '.mp4', '.mkv', '.mov', '.wmv', '.mpeg']
extensionsImage     = ['.jpeg', '.jpg', '.tif', '.png', '.svg', '.webp', '.heic']
extensionGIF        = ['.gif']
extensionsAudio     = ['.wav', '.aiff', '.mp3', '.ogg', '.aac', '.flac', '.m4a']
extensionHAR        = ['.har']
extensionsLogs      = ['.html', '.txt', '.log', '.xlog', '.json', '.htm']
extensionsSetup     = ['.exe', '.msi', '.jar']
extensionsCompress  = ['.zip', '.7z', '.rar', '.iso']
extensionPDF        = ['.pdf']
extensionOffice     = ['.csv', '.docx', '.ppt', '.xlsx', '.pptx']

# * Concat
base_folder    = 'G:/Téléchargements'
vidFiles       = os.path.join(base_folder, 'Vidéos')
imgFiles       = os.path.join(base_folder, 'Images')
gifFiles       = os.path.join(base_folder, 'GIFs')
audioFiles     = os.path.join(base_folder, 'Audios')
harFiles       = os.path.join(base_folder, 'HARs')
logFiles       = os.path.join(base_folder, 'Logs')
exeFiles       = os.path.join(base_folder, 'Setup')
zipFiles       = os.path.join(base_folder, 'Fichiers Compressés')
pdfFiles       = os.path.join(base_folder, 'PDFs')
officeFiles    = os.path.join(base_folder, 'Office')

# ? Lister le contenu du dossier Téléchargement
files = glob.glob(os.path.join(base_folder, "*"))

for file in files:
  # * Identifier les types de fichiers
  extension = os.path.splitext(file)[1].lower()
  # * Déplacer les fichier dans le bon dossier
  if extension in extensionsAudio:
    if(path.exists(audioFiles)):
      shutil.move(file, audioFiles)
    else:
      os.mkdir(audioFiles)
      shutil.move(file, audioFiles)

  if extension in extensionsVideos:
    if(path.exists(vidFiles)):
      shutil.move(file, vidFiles)
    else:
      os.mkdir(vidFiles)
      shutil.move(file, vidFiles)

  if extension in extensionGIF:
    if(path.exists(gifFiles)):
      shutil.move(file, gifFiles)
    else:
      os.mkdir(gifFiles)
      shutil.move(file, gifFiles)

  if extension in extensionsImage:
    if(path.exists(imgFiles)):
      shutil.move(file, imgFiles)
    else:
      os.mkdir(imgFiles)
      shutil.move(file, imgFiles)

  if extension in extensionHAR:
    if(path.exists(harFiles)):
      shutil.move(file, harFiles)
    else:
      os.mkdir(harFiles)
      shutil.move(file, harFiles)

  if extension in extensionsLogs:
    if(path.exists(logFiles)):
      shutil.move(file, logFiles)
    else:
      os.mkdir(logFiles)
      shutil.move(file, logFiles)

  if extension in extensionsSetup:
    if(path.exists(exeFiles)):
      shutil.move(file, exeFiles)
    else:
      os.mkdir(exeFiles)
      shutil.move(file, exeFiles)

  if extension in extensionsCompress:
    if(path.exists(zipFiles)):
      shutil.move(file, zipFiles)
    else:
      os.mkdir(zipFiles)
      shutil.move(file, zipFiles)

  if extension in extensionPDF:
    if(path.exists(pdfFiles)):
      shutil.move(file, pdfFiles)
    else:
      os.mkdir(pdfFiles)
      shutil.move(file, pdfFiles)

  if extension in extensionOffice:
    if(path.exists(officeFiles)):
      shutil.move(file, officeFiles)
    else:
      os.mkdir(officeFiles)
      shutil.move(file, officeFiles)


































