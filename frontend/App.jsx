import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './src/pages/Login'
import RedirectToLogin from './src/pages/RedirectToLogin'
import RedirectPage from './src/pages/RedirectPage'
import Home from './src/pages/Home';

function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<RedirectPage/>} />
        <Route path="/login/" element={<RedirectToLogin/>} />
        <Route path="/login/:id" element={<Login/>} />
        <Route path="/home/:id" element={<Home/>} />
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
