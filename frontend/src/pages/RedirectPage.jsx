import React from 'react'
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'

const RedirectPage = () => {
    const navigate = useNavigate();
    useEffect(() => {
        navigate('/login');
    }, [navigate])
  return (
    <div>RedirectPage</div>
  )
}

export default RedirectPage