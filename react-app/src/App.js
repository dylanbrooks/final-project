import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./index.css"
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import ArtistsList from "./components/ArtistsList"
// import { authenticate } from "./services/auth";
import { authenticate } from "./store/session";
import Search from "./components/Search"
import HomePage from "./components/HomePage"
import ArtistPage from "./components/ArtistPage";
import SongPage from "./components/SongPage";

function App() {
  // const [authenticated, setAuthenticated] = useState(false);
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/" exact={true}>
          <HomePage />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path="/" exact={true}>
          <h1>My Home Page</h1>
        </ProtectedRoute>
        <Route path ='/artists' exact={true}>
          <ArtistsList />
        </Route>
        <Route path ='/search/:searchInput' exact={true}>
          <Search />
        </Route>
        <Route path="/artists/:artistId" exact={true}>
          <ArtistPage />
        </Route>
        <Route path="/artists/:artistId/song/:songId" exact={true}>
          <SongPage />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
