import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'f4d93ea269824dd2bd09bf81777e3764'
CLIENT_SECRET = '712c54a92871429a8376e823db94c16b'
REDIRECT_URI = 'http://localhost:8888/callback'

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-read-private user-top-read user-read-recently-played"
))

# Obtener las canciones más escuchadas
try:
    top_tracks = sp.current_user_top_tracks(limit=50, time_range="short_term")
    top_tracks_ids = {track['id']: idx for idx, track in enumerate(top_tracks['items'])}
except spotipy.exceptions.SpotifyException as e:
    print(f"Error al obtener las canciones más escuchadas: {e}")
    top_tracks_ids = {}

# Obtener las canciones de la playlist con paginación
playlist_url = 'https://open.spotify.com/playlist/1xZH9Wsj4GuN5c4hYr6O4g'  # Cambiar por la URL correcta
playlist_id = playlist_url.split('/')[-1]

playlist_tracks = []
offset = 0
limit = 100
max_tracks = 1000  # Limitamos el número de canciones a obtener

while len(playlist_tracks) < max_tracks:
    try:
        results = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        playlist_tracks.extend(results['items'])
        if len(results['items']) < limit:
            break
        offset += limit
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error al obtener las canciones de la playlist: {e}")
        break

# Crear un diccionario con las canciones y su tiempo de escucha desde el historial de reproducciones recientes
track_play_time = {}

# Obtener el historial de canciones recientemente reproducidas
recently_played = sp.current_user_recently_played(limit=50)

for item in recently_played['items']:
    track_id = item['track']['id']
    
    # Usamos el track_id para contar cuántas veces se ha reproducido
    if track_id in track_play_time:
        track_play_time[track_id] += 1  # Incrementamos la cantidad de veces que se ha escuchado
    else:
        track_play_time[track_id] = 1  # Es la primera vez que se escucha

# Crear un diccionario con las canciones de la playlist y su popularidad basada en las canciones más escuchadas
track_popularity = {}

# Aquí tomamos el 'top_tracks_ids' como el índice para determinar la "popularidad"
# Las canciones con un índice más bajo (más alto en el ranking) serán consideradas más populares
for track in playlist_tracks:
    if track and 'track' in track and track['track']:  # Verificar que 'track' no sea None
        track_id = track['track'].get('id')
        if track_id:
            if track_id in top_tracks_ids:
                # Asignamos el índice de la canción en tu historial de canciones más escuchadas
                track_popularity[track_id] = top_tracks_ids[track_id]

# Ahora vamos a ordenar las canciones por la cantidad de veces que se han escuchado
# Si una canción no tiene un valor en track_play_time, asignamos 0 (menos prioridad)
sorted_tracks = sorted(playlist_tracks, key=lambda x: (
    track_play_time.get(x['track']['id'], 0) + track_popularity.get(x['track']['id'], float('inf'))
) if 'track' in x and x['track'] else 0, reverse=True)

# Imprimir la playlist ordenada por popularidad y número de reproducciones recientes
for track in sorted_tracks:
    if 'track' in track and track['track']:  # Verificar que 'track' no sea None
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        track_url = track['track']['external_urls']['spotify']
        print(f"{track_name} - {artist_name} - {track_url}")
