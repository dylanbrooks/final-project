import React from "react";
import { useHistory, NavLink } from "react-router-dom";
import './CSS/HomePage.css'
import jaoImg from '../jao.jpg'
import ozunaImg from '../ozuna.jpg'
import staycImg from '../stayc.jpg'
import badBunnyImg from '../bad-bunny.png'
import rauwImg from '../rauw.png'
import lagumImg from '../lagum.jpg'



const HomePage = () => {
    const history = useHistory()


    return (
        <>
            <div className="outerDiv">
                <div className="artistText">
                    <h2>N E W &nbsp; &nbsp; R E L E A S E S</h2>
                </div>
                <div className="imgHolder1">
                    <div id="jaoImg">
                        <NavLink to="/song/2" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={jaoImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                    <div id="ozunaImg">
                        <NavLink to="/song/9" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={ozunaImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                    <div id="staycImg">
                        <NavLink to="/song/8" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={staycImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                </div>
                <div className="imgHolder2">
                    <div id="badBunnyImg">
                        <NavLink to="/song/2" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={badBunnyImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                    <div id="rauwImg">
                        <NavLink to="/song/9" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={rauwImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                    <div id="lagumImg">
                        <NavLink to="/song/8" exact={true} activeClassName="active">
                            <img className='homeAlbumImg' src={lagumImg} alt="logo" height="250" />
                        </NavLink>
                    </div>
                </div>
            </div>
        </>

    )
}

export default HomePage;

