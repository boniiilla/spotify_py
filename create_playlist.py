import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = str(input('Introduce tu CLIENT ID:'))
CLIENT_SECRET = str(input('Introduce tu CLIENT SECRET:'))
REDIRECT_URI = str(input('Introduce la REDIRECT URI:'))

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-modify-public playlist-modify-private user-top-read"
))

# Obtener tus canciones más escuchadas con paginación
top_tracks = []
limit = 50  # Límite máximo permitido por la API
offset = 0   # Empezamos desde el primer track
while len(top_tracks) < 400:  # Continuamos hasta obtener 400 canciones
    results = sp.current_user_top_tracks(limit=limit, offset=offset, time_range="short_term")
    top_tracks.extend(results['items'])  # Añadir las canciones a la lista
    
    # Aumentar el offset para la siguiente solicitud
    offset += limit

# Solo tomar las primeras 400 canciones si hay más de 400 (en caso de que haya algún error con el límite)
top_tracks = top_tracks[:400]

# Extraer los IDs de las canciones
track_ids = [track['id'] for track in top_tracks]

# Crear una nueva playlist
user_id = sp.current_user()['id']  # Obtener el ID de usuario
playlist_name = str(input('Como quieres que se llame la playlist? '))  # Nombre de la nueva playlist
playlist_description = str(input('Describe tu playlist: '))

# Crear la playlist
playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

# Dividir los IDs en fragmentos de 100 canciones y agregarlas a la playlist
for i in range(0, len(track_ids), 100):
    track_ids_chunk = track_ids[i:i+100]
    sp.user_playlist_add_tracks(user_id, playlist['id'], track_ids_chunk)

print(f"¡Playlist creada con éxito! Puedes verla aquí: {playlist['external_urls']['spotify']}")
