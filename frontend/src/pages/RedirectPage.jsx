import React from 'react'
import getIP from '../utils/getIP';
import axios from 'axios';
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'


const RedirectPage = () => {
  const [IP, setIP] = useState(null);
  const navigate = useNavigate();
  const backendUrl = "http://localhost:5000";
  async function ipAlredyLogged(ip) {
    try {
      const ipAlredyLoggedResponse = await axios.post(`${backendUrl}/api/login/ip-alredy-logged`, 
        {"ip" : ip}
      ).then((response) => response.data)

      return ipAlredyLoggedResponse
    } catch (error) {
      console.log(error)
      return null
    }
  }

  // Obtem o IP
  useEffect(() => {
    async function fetchIP() {
      setIP(await getIP());
    }
    fetchIP();
  }, [])

  // Cehca no backend se o IP ja está logado
  useEffect(() => {
    async function fetchCheckIp() {
      if (IP) { // Só roda se IP for diferente de null
        console.log(IP)
        const response = await ipAlredyLogged(IP);
        console.log(response)
        
        // Redireciona para a Home
        if (response.logged === "true") {
          navigate(`/home/${response.token}`)
        } else { // Redireciona para o login
          navigate(`/login`)
        }
      }
    }
    fetchCheckIp();

  }, [IP])

    return (
    <div>RedirectPage</div>
  )
}

export default RedirectPage