import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import banner from './banner.png'
import './CSS/NavBar.css'

const NavBar = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchInput, setSearchInput] = useState('');

  const searchFunc = async (e) => {
    e.preventDefault();

    history.push(`/search/${searchInput}`)
  }


  return (
    <nav>
      <div className="barPanel">
        <form className='searchForm'>
          <input
            type='text'
            placeholder='Find an artist'
            onChange={(e) => setSearchInput(e.target.value)}></input>
          <button id='searchButton' onClick={searchFunc}>Search</button>
        </form>
        <div id="homeButton">
            <NavLink to="/" exact={true} activeClassName="active">
              <img src={banner} alt="logo" height="60" />
            </NavLink>
        </div>
        <div className="loginButton">
            <NavLink to="/login" exact={true} activeClassName="active">
              Login
                </NavLink>
        </div>
        <div className="signupButton">
            <NavLink to="/sign-up" exact={true} activeClassName="active">
              Sign Up
            </NavLink>
          </div>
          <div>
          </div>
        <LogoutButton />
      </div>
    </nav>
  );
}

export default NavBar;
