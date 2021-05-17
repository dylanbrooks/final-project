import React, { useEffect, useState } from "react";
import { NavLink, useParams } from "react-router-dom";
import jaoImg from '../jao-artist.jpg'
import './CSS/ArtistPage.css'
import jaoAlbumImg from '../jao.jpg'

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
                <NavLink to={`/song/${song.id}`}>{song.name}</NavLink>
            </li>
        );
    });

    return (
        <>
            <div className="topDiv">
                <img src={jaoAlbumImg} />
            </div>
            <div className='artistOuterDiv'>
                <div>
                    <img id="jaoImg" src={jaoImg} alt="logo" height="250" />
                </div>
                <div className='songListDiv'>
                    <h1>Songs: </h1>
                    <ul>{songList}</ul>
                </div>
            </div>
        </>
    );
}

export default ArtistPage;