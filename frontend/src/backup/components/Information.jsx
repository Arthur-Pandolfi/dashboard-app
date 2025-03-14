import React, { forwardRef} from 'react'
import axios from 'axios';

const information = forwardRef(({ id, information, text }, ref) => {
  return (
    <div className="information__global">
      <div ref={ref} className="information__container--outside">
        <div className="information__container--inside">
          <div className="information__id_and_text">
            <p className="information__id">{id}</p>
            <p className="information__information">{information}</p>
          </div>
	          <button className="information__text">{text}</button>
        </div>
      </div>
    </div>
  )
});

export default information

