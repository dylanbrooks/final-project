import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import { login } from '../store/session'
import banner from './banner.png'
import './CSS/NavBar.css'

const NavBar = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchInput, setSearchInput] = useState('');
  const user = useSelector(state => state.session.user)

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
          <button id='searchButton' onClick={searchFunc}>SEARCH</button>
        </form>
        <div id="homeButton">
            <NavLink to="/" exact={true} activeClassName="active">
              <img src={banner} alt="logo" height="60" />
            </NavLink>
        </div>
        {!user &&
        <>
        <div className="loginButton">
            <NavLink id='loginButton' to="/login" exact={true} activeClassName="active">
              LOG IN
            </NavLink>
        </div>
        <div className="demoLogin">
            <button id='demoLoginButton' onClick={async (e) => { await dispatch(login('demo@aa.io', 'password')) }}>
              DEMO LOG IN
            </button>
        </div>
        </>
          }
          {!user &&
        <div className="signupButton">
            <a id='signupButton' href="/sign-up" exact={true} activeClassName="active">
              SIGN UP
            </a>
          </div>
        }
          <div>
          </div>
         {user && 
         <div id='logoutButtonDiv'>
        <LogoutButton />
        </div>
         }
      </div>
    </nav>
  );
}

export default NavBar;
