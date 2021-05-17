import React, { useState } from "react";
import  { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import '../CSS/Login.css'

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <>
      <h1 id='loginText'>LOG IN</h1>
      <div className='formDiv'>
        <form id='loginForm' onSubmit={onLogin}>
          <div>
            {errors.map((error) => (
              <div>{error}</div>
            ))}
          </div>
          <div>
            <label className='loginLabels' htmlFor="email">Email</label>
            <br />
            <input
              name="email"
              type="text"
              placeholder="Email"
              value={email}
              onChange={updateEmail}
            />
          </div>
          <div>
            <label className='loginLabels' htmlFor="password">Password</label>
            <br />
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={password}
              onChange={updatePassword}
            />
            <br />
            <button id='loginSubmitButton' type="submit">Login</button>
          </div>
        </form>
      </div>
    </>
  );
};

export default LoginForm;
