import React from 'react';

const Button = ({ children, onClick, type = 'button' }) => (
  <button
    onClick={onClick}
    type={type}
    className="metallic-button text-white font-bold py-2 px-4 rounded transition duration-300"
  >
    {children}
  </button>
);

export default Button;
