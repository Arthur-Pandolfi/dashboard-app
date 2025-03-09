import axios from "axios";

export default async function getIP() {
  /** 
   * Função para obter o IP do usuário
   * 
   * @returns {string} - IP do usuário
   *  */  
  
  try {
      const response = await axios.get("https://api.ipify.org?format=json")
      return response.data.ip
    } catch (error) {
      console.log(error)
      return null
    }
  }