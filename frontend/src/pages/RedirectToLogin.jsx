import React, { useState } from 'react';
import axios from 'axios';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const RedirectToLogin = () => {
  const backendURL = "http://localhost:5000";
  const [id, setID] = useState(null);
  const navigate = useNavigate();

  async function getID() {
    try {
      const response = await axios.get(`${backendURL}/api/login/generate-id`);
      setID(response.data.id_login);
    } catch (error) {
        setID(error.message);
        console.log(error.message);
    }
  }

  useEffect(() => {
    getID();
  }, []);


  return (
    <div>
      <h1>Redirecting</h1>
      <p>{id}</p>
      {id ? navigate(`/login/${id}`) : null}
    </div>
  )
}

export default RedirectToLogin;
