# Spotify Playlist Manager

Este repositorio contiene dos scripts en Python que interactúan con la API de Spotify para gestionar y personalizar tus listas de reproducción. Los programas permiten:

1. **Ordenar canciones por popularidad**: Organiza las canciones de una playlist específica según cuán escuchadas estén en tu biblioteca personal de Spotify.
   
2. **Crear una playlist con tus canciones más escuchadas**: Crea automáticamente una nueva playlist con tus canciones más escuchadas, basada en tus datos personales de Spotify.

## Funcionalidades

### 1. **Ordenar canciones más escuchadas**
   - Ordena las canciones de una playlist de Spotify según la popularidad de las canciones en tu biblioteca personal.
   - Utiliza la API de Spotify para obtener las canciones más escuchadas y luego organiza las canciones de la playlist en base a esta popularidad.

### 2. **Crear playlist con canciones más escuchadas**
   - Crea una nueva playlist con tus 400 canciones más escuchadas de Spotify.
   - Agrega las canciones a la nueva playlist dividiendo la carga en fragmentos para ajustarse a los límites de la API de Spotify.
   - Obtén la URL de la nueva playlist para acceder a ella fácilmente.

## Requisitos

- Python 3.8 o superior
- Dependencias necesarias:
  - `spotipy` (para interactuar con la API de Spotify)

Puedes instalar las dependencias ejecutando:

```bash
pip install spotipy
```

## Configuración

1. **Crear una cuenta de desarrollador en Spotify**:
   - Dirígete a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) para crear una aplicación y obtener las credenciales necesarias (CLIENT_ID, CLIENT_SECRET y REDIRECT_URI).

2. **Configura las credenciales en los scripts**:
   - Abre los archivos de Python (`order_list.py` o `create_playlist.py`) y reemplaza las credenciales con las tuyas.

## Uso

1. **Para ordenar las canciones de una playlist**:
   - Modifica el enlace de la playlist en el script.
   - Ejecuta el script y obtendrás las canciones ordenadas según tu popularidad.

2. **Para crear una nueva playlist con tus canciones más escuchadas**:
   - Ejecuta el script para crear una playlist automática con tus canciones más escuchadas.

## Notas

- Ambos scripts requieren autenticación mediante OAuth con tu cuenta de Spotify.
- Es posible que necesites interactuar con el navegador para autorizar el acceso de la aplicación a tus datos de Spotify.

---

Este repositorio es ideal para quienes quieren personalizar sus playlists y gestionar su biblioteca de Spotify de una manera más dinámica y adaptada a sus gustos y hábitos de escucha.

¡Contribuciones son bienvenidas! Si tienes ideas para mejorar estos scripts o corregir problemas, no dudes en abrir un *issue* o hacer un *pull request*.

---

Esta descripción puede ser utilizada en la página principal de tu repositorio para darle a los usuarios una idea clara de lo que hace el proyecto y cómo usarlo.
