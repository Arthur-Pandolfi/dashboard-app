import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useParams } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();
  const { id } = useParams();

  function redirectToShowInfoPage() {
    navigate(`/home/${id}/ShowInformation`)
  }

  function redirectToAddProductPage() {
    navigate(`/home/${id}/AddProduct`)
  }

  function redirectToAddSalePage() {
    navigate(`/home/${id}/AddSale`)
  }

  return (
    <div className="home__global">
      <div className="home__options">
          <button className='home__options--show_info--button' type='button' onClick={redirectToShowInfoPage}>Mostrar Informações</button>
          <button className='home__options--add_product--button' type="button" onClick={redirectToAddProductPage}>Adicionar Produto</button>
            <button className='home__options--add_sale--button' type="button" onClick={redirectToAddSalePage}>Adicionar Venda</button>
      </div>
    </div>
  )
}

export default Home