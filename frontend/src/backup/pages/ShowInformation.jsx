import React from 'react'
import Information from '../components/information'
import { useState, useRef } from 'react'
import { useEffect } from 'react'

const ShowInformation = () => {
  const [count, setCount] = useState(1);
  const ref = useRef(null);

  useEffect(() => {
    function updateCount() {
      if (ref.current) {
        const windowHeight = window.innerHeight;
        const componentHeight = ref.current.clientHeight || 1;
        const items = Math.ceil(windowHeight / componentHeight);
        setCount(items);
      }
    };

    updateCount();
    window.addEventListener('resize', updateCount);

    return() => {window.removeEventListener("resize", updateCount)}
  }, []
)

  return (
    <>
      <Information ref={ref} id="1" information="Abc" text="abc"/>

      {Array.from({ length: count - 1}).map((_, index) => (
        <Information key={index} id="1" information="Abc" text="abc"></Information>
      ))}
    </>
  )
}

export default ShowInformation
