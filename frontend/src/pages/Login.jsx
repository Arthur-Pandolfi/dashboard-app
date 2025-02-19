import React from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  function submitLogin() {
    console.log("Login efetuado com sucesso");
    navigate("/home");
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
