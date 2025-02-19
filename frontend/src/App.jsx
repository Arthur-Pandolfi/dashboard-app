import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/login'
function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path='/home' element={<h1>Home</h1>}/>
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
