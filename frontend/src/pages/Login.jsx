import React from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();
  async function submitLogin() {
    try {
      const response = await axios.get("http://localhost:5000/api/login/request", {user: "user123", password: "Password"})
      console.log(response)
      
      } catch (error) {
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
            <input className="login__user-input" type="email" placeholder="User123"/>
            <br />
            <label className="login__password-label" htmlFor="password">Senha</label>
            <input className="login__password-input" type="password" placeholder="Password123"/>
            <br/>
            <button className="login__submit-button" type="button" onClick={submitLogin}>Entrar</button>
          </div>
        </div>
      </div>
    </>
  );
};
  
//Adicionar função de bloquear os campoos e o botão quando houver um request

export default Login;
