import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { createTranslation, getTranslation } from "../store/song"
import './CSS/SongPage.css'

function SongPage() {
    const [song, setSong] = useState({});
    const [translation, setTranslation] = useState('');
    const [startIndex, setStartIndex] = useState();
    const [stopIndex, setStopIndex] = useState();
    const userId = useSelector(state => state.session.user.id);
    const trans = useSelector(state => state.songStorage.trans)
    const songId = useParams();
    const dispatch = useDispatch();

    useEffect(() => {
        async function fetchData() {
            const response = await fetch(`/api/songs/${songId.songId}`);
            const responseData = await response.json();
            await setSong(responseData.song);
        }
        fetchData();
        if (!trans) {
            dispatch(getTranslation(songId))
        }
    }, [trans, dispatch]);

    console.log(trans)

    const TransCreation = async (e) => {
        e.preventDefault();
        const newTrans = await dispatch(createTranslation({
            translation,
            startIndex,
            stopIndex,
            userId,
            songId: song.id
        }))
        console.log('submitted')
    }

    const collectText = (e) => {
        const lyrics = song.lyrics;
        const highlightedText = window.getSelection().toString();
        const textLength = highlightedText.length;

        const firstIndex = lyrics.indexOf(highlightedText);
        const lastIndex = (textLength - 1) + firstIndex;

        setStartIndex(firstIndex);
        setStopIndex(lastIndex);

    }

    return (
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
            <div dangerouslySetInnerHTML={{ __html: song.lyrics }} onMouseUp={collectText}></div>
                {/* <div> {song.lyrics} </div> */}
            </div>
                <form id='transForm' onSubmit={TransCreation}>
                    <div id='translationForm'>
                        <label id='translationForm'>Enter Translation:</label>
                    <input
                        type='hidden'
                        name='startIndex'
                        value={startIndex}></input>
                    <input
                        type='hidden'
                        name='stopIndex'
                        value={stopIndex}></input>
                    <input
                        type='hidden'
                        name='userId'
                        value={userId}></input>
                    <input
                        type='hidden'
                        name='songId'
                        value={song.id}></input>
                        <input
                            type='text'
                            name='translation'
                            onChange={(e) => setTranslation(e.target.value)}
                        ></input>
                        <button id='transFormButton'
                        type='submit'
                        > Add Translation </button>
                    </div>
                </form>
        </>
    );
}

export default SongPage;