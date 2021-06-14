import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { createTranslation, createComment, getComments, getTranslation } from "../store/song"
import './CSS/SongPage.css'

function SongPage() {
    const [song, setSong] = useState({});
    const [translation, setTranslation] = useState('');
    const [startIndex, setStartIndex] = useState();
    const [stopIndex, setStopIndex] = useState();
    const [comment, setComment] = useState();
    const comments = useSelector(state => state.songStorage.comment)
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
        if (!comments) {
            dispatch(getComments(songId))
        }
    }, [trans, comments, dispatch]);

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

    const CommentCreation = async (e) => {
        e.preventDefault();
        const newComment = await dispatch(createComment({
            comment,
            userId,
            songId: song.id
        }))
        console.log('comment submitted')
    }

    console.log(comments)

    const collectText = (e) => {
        const lyrics = song.lyrics;
        const highlightedText = window.getSelection().toString();
        const textLength = highlightedText.length;

        const firstIndex = lyrics.indexOf(highlightedText);
        const lastIndex = (textLength - 1) + firstIndex;

        console.log(highlightedText)
        console.log(firstIndex)
        console.log(lastIndex)

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
            {/* <div dangerouslySetInnerHTML={{ __html: song.lyrics }} onMouseUp={collectText}></div> */}
                <div className='lyricsDiv' onMouseUp={collectText}> {song.lyrics} </div>
            </div>
                <form id='transForm' onSubmit={TransCreation}>
                    <div id='translationForm'>
                        <label id='translationFormLabel'>Enter Translation:</label>
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
                <form id='commentForm' onSubmit={CommentCreation}>
                    <div id='commentForm'>
                        <label id='commentFormLabel'>Enter Comment:</label>
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
                        name='comment'
                        onChange={(e) => setComment(e.target.value)}
                    ></input>
                    <button id='commentFormButton'
                        type='submit'
                    > Post Comment </button>
                    </div>
                </form>
                {/* {trans?.map(trans => (
                    // return (
                    <div id='commentListDiv'>
                        {trans.trans}
                    </div>
                    // )
                ))} */}
                {comments?.map(comment => (
                    // return (
                        <div id='commentListDiv'>
                            {comment.username}
                            {comment.comment}
                        </div>
                    // )
                ))}

        </>
    );
}

export default SongPage;