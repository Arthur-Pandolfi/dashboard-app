import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './src/pages/Login'
import RedirectToLogin from './src/pages/RedirectToLogin'
import RedirectPage from './src/pages/RedirectPage'
import Home from './src/pages/Home';
import ShowInformation from './src/pages/ShowInformation'
import AddProduct from './src/pages/AddProduct'
import AddSale from './src/pages/AddSale'

function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<RedirectPage/>} />
        <Route path="/login/" element={<RedirectToLogin/>} />
        <Route path="/login/:id" element={<Login/>} />
        <Route path="/home/:id" element={<Home/>} />
        <Route path="/home/:id/ShowInformation" element={<ShowInformation/>} />
        <Route path="/home/:id/AddProduct" element={<AddProduct/>} />
        <Route path="/home/:id/AddSale" element={<AddSale/>} />

      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
