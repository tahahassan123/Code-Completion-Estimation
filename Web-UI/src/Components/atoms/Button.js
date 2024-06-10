import React from 'react';

const Button = ({ children, onClick }) => (
  <button
    onClick={onClick}
    className="bg-metallic-gradient hover:bg-metallic-shiny text-white font-bold py-2 px-4 rounded transition duration-300 shadow-metallic border border-transparent hover:border-metallic-light"
  >
    {children}
  </button>
);

export default Button;