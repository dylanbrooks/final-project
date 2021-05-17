import React from "react";
import { useHistory, NavLink } from "react-router-dom";
import './CSS/HomePage.css'
import jaoImg from '../jao.jpg'
import ozunaImg from '../ozuna.jpg'
import staycImg from '../stayc.jpg'



const HomePage = () => {
    const history = useHistory()


    return (
        <>
            <div className="outerDiv">
                <div className="artistText">
                    <h2>new releases</h2>
                </div>
                <div className="imgHolder">
                    <div id="jaoImg">
                        <NavLink to="/song/5" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={jaoImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                    <div id="ozunaImg">
                        <NavLink to="/" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={ozunaImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                    <div id="staycImg">
                        <NavLink to="/" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={staycImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                </div>
            </div>
        </>

    )
}

export default HomePage;

