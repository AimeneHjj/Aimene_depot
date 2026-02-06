#########################################################
#import du package os
#import os
#cwd = os.getcwd() 
#print("Current working directory:", cwd)
###########################################################
#import du package requests
#import requests
#response = requests.get("https://fastly.picsum.photos/id/108/800/600.jpg?hmac=V8hp5ux4MrCAodw4swnpj6zLHnRAhWngQRzTupFX_Ac")
#print(response.status_code)
#"print(response.content)

#############################################################
#Etape1
#directory = "images"
#parent_dir = "C:\Users\hejja\Documents\ISARA\4A\OPEN2026"
#path = os.path.join (parent_dir,directory)
#os.mkdir(path)
#print("Directory '%s' created" %directory)
#directory = "images"
#parent_dir = "C:\Users\hejja\Documents\ISARA\4A\OPEN2026"
#mode = 0o666
#path = os.path.join (parent_dir,directory)
#os.mkdir(path,mode)
#print("Directory '%s' created" %directory)

#with open("C:\Users\hejja\Documents\ISARA\4A\OPEN2026/images/image1.jpg", "wb") as f:
#f.write(response.content)
#print("Image saved successfully.")
##################################################################
#Etape 2
#import os
#from moviepy.editor import *
#créer des variables pour :
#- dossier images (celui qui a été généré hier)
#- nom du fichier audio (choisissez en un qui vous plaît :))
#- nom du diaporama obtenu à la sortie du script

#fichier_audio = "Audio.mp3"

#Diapo = "nature.mp4"
#images_utiles = []

#for fichier in os.listdir(dossier_images):
#if fichier.endswith(".jpg"):
#chemin_image = os.path.join(dossier_images, fichier)
#images_utiles.append(chemin_image)
#print("Image ajoutée :", chemin_image)

#Créer une liste (donc entre crochets) des images à utiliser

#Créer une liste de clips (avec même taille pour chaque image) -> cf. doc de moviepy (lien dans le sujet)

#Concaténer les clips pour former la vidéo
#-> cf. doc de moviepy (lien dans le sujet)

#Charger la musique dans le clip

#Ajouter l'audio à la vidéo

#Générer le diaporama

#Faites en sorte que ce script appelle le script d'hier (qui sera donc défini comme une fonction) avec des paramètres et un retour adapté

###########

#####################################################################################
#Etape1 (Prof)
import os
import requests

script_dir = os.path.dirname(os.path.abspath(__name__))
os.chdir(script_dir)

# Créer dossier (s'il n'existe pas) pour sauvegarder les images
dossier_images = "images_picsum"
if os.path.exists(dossier_images) == False :
    os.makedirs(dossier_images)

# Demander à l'utilisateur le nombre d'images souhaité
nbImages = input("Combien voulez-vous d'images ? ")

# Télécharger le nombre d'images aléatoires souhaité
for i in range(1, int(nbImages) + 1):
    # créer l'URL
    url = "https://picsum.photos/800/600?random=" + str(i)
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # créer le path d'accès à chaque image
            path_image = os.path.join(dossier_images, "image_" + str(i) + ".jpg")
            # ouvrir le fichier en binaire
            fichier = open(path_image, 'wb')
            # écrire la contenu du retour de la requête
            fichier.write(response.content)
            # fermer le fichier
            fichier.close()
            # témoin de sauvegarde dans la console
            print("Image", str(i), "sauvegardée avec succès !")
    except Exception as e:
        print("Erreur pour l'image", str(i),  ":", str(e))

####################################################################################
####################################################################################
###################################################
#Etape 2 (prof)
from moviepy.editor import *
import os

# Dossier contenant les images
dossier_images = "images_picsum"
# Chemin vers le fichier audio
fichier_audio = "Bowie, David - Life On Mars.mp3"
# Durée d'affichage de chaque image (en secondes)
duree_par_image = 3
# Chemin de sortie pour la vidéo
sortie_video = "diaporama.mp4"

# Récupérer la liste des images dans le dossier
images = []
listeImages = os.listdir(dossier_images)
nbImages = len(listeImages)
for i in range(0, nbImages) :
    fichier = listeImages[i]
    if fichier.lower().endswith(('.jpg', '.jpeg', '.png')):
        chemin_image = os.path.join(dossier_images, fichier)
        images.append(chemin_image)

# Pister si erreur
print("Nombre d'images trouvées",len(images))
if len(images) == 0:
    print("ERREUR : Aucune image trouvée !")
    sys.exit(1)

# Créer une liste de clips avec même taille pour chaque image
clips = []
for image in images:
    print("Traitement de :", image)
    clip = ImageClip(image).set_duration(duree_par_image)
    clip = clip.resize(height=720)  # Uniformiser la hauteur
    clips.append(clip)

# Concatenation des clips pour former la vidéo
video = concatenate_videoclips(clips, method="compose")

# Charger la musique
audio = AudioFileClip(fichier_audio)

# Ajouter la musique à la vidéo (en ajustant la durée si nécessaire)
if audio.duration < video.duration:
    # Si la musique est plus courte que la vidéo, on la boucle
    audio = afx.audio_loop(audio, duration=video.duration)
elif audio.duration > video.duration:
    # Si la musique est plus longue, on la coupe
    audio = audio.subclip(0, video.duration)

# Ajouter l'audio à la vidéo
video_final = video.set_audio(audio)

# Écrire la vidéo finale
# video_final.write_videofile(
#     sortie_video, # nom du fichier de sortie (obligatoire)
#     fps=24,       # nombre d'images par seconde
#     threads=4,    # nombre de threads pour l'encodage
#     preset='medium', # vitesse d'encodage : ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
#     audio_codec="aac" # codec audio

video_final.write_videofile(sortie_video, fps = 24)

print("Diaporama généré avec succès", sortie_video)
