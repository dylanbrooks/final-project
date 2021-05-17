import React, { useEffect, useState } from "react";
import { NavLink, useParams } from "react-router-dom";
import jaoImg from '../jao-artist.jpg'
import './CSS/SongPage.css'

function SongPage() {
    const [song, setSong] = useState({});
    const songId = useParams();
    useEffect(() => {
        async function fetchData() {
            const response = await fetch(`/api/songs/${songId.songId}`);
            const responseData = await response.json();
            await setSong(responseData.song);
        }
        fetchData();
    }, []);

    // const songFunc = (song) => {
    //     return (
    //         <>
    //         {song.lyrics}
    //         </>
    //     );
    // };

    return (
        console.log(song),
        <>
            <div className='topDiv'>
                <img src={song.albumArtUrl} />
            </div>
            <div className="artistOuterDiv">
            <div>
                <img id="albumArt" src={song.albumArtUrl} alt="logo" height="250" />
            </div>
            <div id="songName">
                <h1>{song.name}</h1>
            </div>
            </div>
            <div id='lyricsDiv'>
            <h2>Lyrics: </h2>
            <div dangerouslySetInnerHTML={{ __html: song.lyrics }}></div>
            </div>
        </>
    );
}

export default SongPage;