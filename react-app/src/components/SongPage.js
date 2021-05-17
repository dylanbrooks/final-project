import React, { useEffect, useState } from "react";
import { useHistory, NavLink } from "react-router-dom";
import './CSS/SongPage.css'
import jaoImg from '../jao.jpg'




const SongPage = () => {



    return (
        <>
            <div className='outerDiv'>
                <div className='topDiv' />
                <img className='AlbumImg' src={jaoImg} height='300px' width='300px' />
                <div className='ArtistText'>
                    Jão
                </div>
                <div className='SongText'>
                    Me Beija Com Raiva
                </div>
                <div className='lyrics'>
                    The lyrics will go here.
                </div>
            </div>
        </>
    )
}


export default SongPage;