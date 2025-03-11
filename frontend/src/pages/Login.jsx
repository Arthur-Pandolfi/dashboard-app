import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useState, useRef } from "react";
import { useParams } from "react-router-dom";
import encryptData from "../utils/encrtpytData";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();
  const userInput = useRef(null);
  const passwordInput = useRef(null);
  const backendUrl = "http://localhost:5000";
  const { id } = useParams();
  const [IP, setIP] = useState(null);
  const [fieldsDisabled, setFieldsDisabled] = useState(false);
  const [userNotFoundErrorIsDisabled, setUserNotFoundErrorIsEnabled] = useState(false);

  useEffect(() => {
    async function fetchIP() {
      const ip = await getIP();
      setIP(ip);
    }
    fetchIP();
  }, [])

  async function getIP() {
    try {
      const response = await axios.get("https://api.ipify.org?format=json")
      return response.data.ip
    } catch (error) {
      console.log(error)
      return null
    }
  }

  async function submitLogin() {
    try {
      const generateAesKeyResponse = await axios.post(`${backendUrl}/api/keyDB/get-and-store-aes-key`, {"ip" : IP, "loginID": id}).then((response) => response.data)
      const aesKey = generateAesKeyResponse.aes_key
      const encrtpytedData = encryptData(JSON.stringify({user: userInput.current.value, password: passwordInput.current.value}), aesKey)
      setFieldsDisabled(true)
      const loginResponse = await axios.post(`${backendUrl}/api/login/submit-login`, {
        "data": encrtpytedData, 
        "loginId": id,
        "ip": IP,
      });
      const response5 = await axios.post(`${backendUrl}/api/home/getInformations`, {"ip": IP}).then((response) => response.data)
      console.log(response5)
      setFieldsDisabled(false)
      if (loginResponse.data.message === "Login successful") {
        navigate(`/home/${loginResponse.data.token}`)
      } else if (loginResponse.data.message === "User not found") {
        setUserNotFoundErrorIsEnabled(true)
      }
      
      } catch (error) {
        console.log("Server error")
        console.log(error)
    }

  }
  return (
    <>
      <div className="login__extern-container">
        <div className="login__container">
          <h1 className="login__tittle">Login</h1>
          <div className="login__fiels">
            <label className="login__user-label" htmlFor="email">Usuário</label>
            <input className="login__user-input" ref={userInput} type="email" placeholder="User123"disabled={fieldsDisabled}/>
            <br/>
            <label className="login__password-label" htmlFor="password">Senha</label>
            <input className="login__password-input" ref={passwordInput} type="pa:ssword" placeholder="Password123" disabled={fieldsDisabled}/>
            <br/>
            <button className="login__submit-button" type="button" onClick={submitLogin} disabled={fieldsDisabled}>Entrar</button>
            <p className={userNotFoundErrorIsDisabled ? "login__error" : "hidden"} >Usuário não encontrado</p>
          </div>
        </div>
      </div>
    </>
  );
};
  
export default Login;
