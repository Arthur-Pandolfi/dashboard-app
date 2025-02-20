import React from "react";
import { useNavigate } from "react-router-dom";
import { useState, useRef } from "react";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();
  const [isDisabled, setIsDisabled] = useState(false);
  const userInput = useRef(null);
  const passwordInput = useRef(null);
  async function submitLogin() {
    try {
      const response = await axios.post("http://localhost:5000/api/login/", {user: userInput.current.value, password: passwordInput.current.value});
      
      if (response.data.message === "Login successful") {
        navigate("/home")
      } 
      
      } catch (error) {
        setIsDisabled(true)
        console.log("Usuario não encontrado")
    }

  }
  return (
    <>
      <div className="login__extern-container">
        <div className="login__container">
          <h1 className="login__tittle">Login</h1>
          <div className="login__fiels">
            <label className="login__user-label" htmlFor="email">Usuário</label>
            <input className="login__user-input" ref={userInput} type="email" placeholder="User123"/>
            <br />
            <label className="login__password-label" htmlFor="password">Senha</label>
            <input className="login__password-input" ref={passwordInput} type="password" placeholder="Password123"/>
            <br/>
            <button className="login__submit-button" type="button" onClick={submitLogin}>Entrar</button>
            <p className={isDisabled ? "login__error" : "hidden"}>Usuário não encontrado</p>
          </div>
        </div>
      </div>
    </>
  );
};
  
//Adicionar função de bloquear os campoos e o botão quando houver um request

export default Login;
