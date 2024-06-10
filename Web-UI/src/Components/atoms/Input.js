import React from 'react';

const Input = ({ value, onChange, type = 'text' }) => (
  <input
    type={type}
    value={value}
    onChange={onChange}
    className="w-full mt-1 block rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
  />
);

export default Input;