import React from "react";
import { useNavigate } from "react-router-dom";
import { useState, useRef } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { encryptData } from "../utils/encrtpytData";

const Login = () => {
  const navigate = useNavigate();
  const [userNotFoundErrorIsDisabled, setUserNotFoundErrorIsEnabled] = useState(false);
  const userInput = useRef(null);
  const passwordInput = useRef(null);
  const { id } = useParams();
  const backendUrl = "http://localhost:5000";
  async function submitLogin() {
    try {
      const generateAesKeyResponse = await axios.post(`${backendUrl}/api/keyDB/get-and-store-aes-key`, {"ip" : "127.0.0.1", "loginID": id}).then((response) => response.data)
      const aesKey = generateAesKeyResponse.aes_key
      console.log(aesKey)
      const encrtpytedData = encryptData(JSON.stringify({user: userInput.current.value, password: passwordInput.current.value}), aesKey)
      const loginResponse = await axios.post(`${backendUrl}/api/login/submit-login`, {"data": encrtpytedData, "loginId": id});

      if (loginResponse.data.message === "Login successful") {
        navigate("/home")
      } 
      
      } catch (error) {
        setUserNotFoundErrorIsEnabled(true)
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
            <br/>
            <label className="login__password-label" htmlFor="password">Senha</label>
            <input className="login__password-input" ref={passwordInput} type="password" placeholder="Password123"/>
            <br/>
            <button className="login__submit-button" type="button" onClick={submitLogin}>Entrar</button>
            <p className={userNotFoundErrorIsDisabled ? "login__error" : "hidden"}>Usuário não encontrado</p>
          </div>
        </div>
      </div>
    </>
  );
};
  
//Adicionar função de bloquear os campoos e o botão quando houver um request

export default Login;
