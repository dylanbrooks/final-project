import React, { useEffect, useState } from "react";
import { NavLink, useParams } from "react-router-dom";

function ArtistPage() {
    const [songs, setSongs] = useState([]);
    const artistId = useParams();
    useEffect(() => {
        async function fetchData() {
            console.log(artistId.artistId)
            const response = await fetch(`/api/artists/${artistId.artistId}`);
            const responseData = await response.json();
            setSongs(responseData.songs);
        }
        fetchData();
    }, []);

    const songList = songs.map((song) => {
        return (
            <li key={song.id}>
                <NavLink to={`/artists/${song.id}`}>{song.name}</NavLink>
            </li>
        );
    });

    return (
        <>
            <h1>Songs: </h1>
            <ul>{songList}</ul>
        </>
    );
}

export default ArtistPage;