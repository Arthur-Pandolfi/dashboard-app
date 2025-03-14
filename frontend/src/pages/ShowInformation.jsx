import React from 'react'
import axios from 'axios';

const ShowInformation = () => {
  async function download() {
      const url = 'https://drive.usercontent.google.com/u/0/uc?id=1Qy_DoRdYZWU6AcSeOe2hcoLAN5RcL_wR&export=download';
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'SPIKE_APP.msi'); // Pode ser ignorado se o servidor não suportar
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
  };
  
  return(
    <>
      <div className="information__global">
        <button type='button' className="information__download--button" onClick={download}>Download</button>
      </div>
    </>
  )
}

export default ShowInformation
