from typing import NamedTuple


class Version(NamedTuple):
    """Represents the version of the MPD server."""

    major: int
    minor: int
    patch: int


class Status(NamedTuple):
    """Represents the status of the MPD server."""

    state: str
    time: int
    elapsed: int
    bitrate: str
    mixrampdb: str
    mixrampdelay: str
    audio: str
    error: str
    repeat: bool
    random: bool
    single: bool
    consume: bool
    volume: int
    playlist: int
    playlistlength: int
    song: int
    songid: int
    nextsong: int
    nextsongid: int
    duration: int
    xfade: int
    updating_db: int


class Song(NamedTuple):
    """Represents a song in the MPD server."""

    file: str
    title: str
    name: str
    pos: int
    id: int


class Playlist(NamedTuple):
    """Represents a playlist in the MPD server."""

    name: str
    songs: list[Song]
