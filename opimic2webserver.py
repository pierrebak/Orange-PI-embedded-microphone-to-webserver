from flask import Flask, Response, render_template_string
import subprocess

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Orange Pi Live Audio</title></head>
<body style="text-align:center; padding-top:50px;">
    <h1>Microphone en Direct</h1>
    <audio controls autoplay>
        <source src="/audio_feed" type="audio/mpeg">
        Votre navigateur ne supporte pas l'audio live.
    </audio>
    <p>Statut : <span style="color:green;">En direct</span></p>
</body>
</html>
'''

def generate_audio():
    # Commande FFmpeg pour capturer ALSA et sortir du MP3 sur stdout
    # -f alsa : source
    # -i default : micro par défaut
    # -acodec libmp3lame : encodage mp3 (plus compatible web)
    # -f mp3 : format de sortie
    command = [
        'ffmpeg',
        '-f', 'alsa',
        '-i', 'default',
        '-acodec', 'libmp3lame',
        '-ab', '64k', # Débit binaire (léger pour le CPU)
        '-ac', '1',   # Mono
        '-f', 'mp3',
        'pipe:1'      # Envoie vers la sortie standard (stdout)
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    try:
        while True:
            data = process.stdout.read(1024)
            if not data:
                break
            yield data
    finally:
        process.kill()

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/audio_feed')
def audio_feed():
    return Response(generate_audio(), mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)
