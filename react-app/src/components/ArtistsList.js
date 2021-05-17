import React, { useEffect, useState } from "react";
import { NavLink, useParams } from "react-router-dom";

function ArtistList() {
    const [song, setSongs] = useState([]);
    const artistId = useParams();
    useEffect(() => {
        async function fetchData() {
            const response = await fetch(`/api/artists/${artistId}`);
            const responseData = await response.json();
            setSongs(responseData.songs);
        }
        fetchData();
    }, []);

    const songs = songs.map((song) => {
        return (
            <li key={song.id}>
                <NavLink to={`/artists/${song.id}`}>{song.name}</NavLink>
            </li>
        );
    });

    return (
        <>
            <h1>Songs: </h1>
            <ul>{song}</ul>
        </>
    );
}

export default ArtistList;