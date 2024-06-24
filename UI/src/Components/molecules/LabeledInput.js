import React from 'react';
import { Controller } from 'react-hook-form';

const LabeledInput = ({ label, name, type, control, error, options }) => (
  <div className="mb-4">
    <label htmlFor={name} className="block text-sm font-medium text-white mb-2">{label}</label>
    <Controller
      name={name}
      control={control}
      render={({ field }) => {
        switch (type) {
          case 'select':
            return (
              <select
                {...field}
                id={name}
                className="bg-gray-800 text-gray-300 border border-gray-600 rounded-md px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
              >
                {options.map(option => (
                  <option key={option.value} value={option.value}>{option.label}</option>
                ))}
              </select>
            );
          case 'checkbox':
            return (
              <input
                {...field}
                type="checkbox"
                id={name}
                checked={field.value}
                className="form-checkbox h-5 w-5 text-blue-600"
              />
            );
          case 'radio':
            return (
              <div>
                {options.map(option => (
                  <label key={option.value} className="inline-flex items-center">
                    <input
                      {...field}
                      type="radio"
                      value={option.value}
                      checked={field.value === option.value}
                      className="form-radio h-4 w-4 text-blue-600"
                    />
                    <span className="ml-2">{option.label}</span>
                  </label>
                ))}
              </div>
            );
          default:
            return (
              <input
                {...field}
                type={type}
                id={name}
                className="bg-gray-800 text-gray-300 border border-gray-600 rounded-md px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
              />
            );
        }
      }}
    />
    {error && <p className="text-red-500 text-xs mt-1">{error.message}</p>}
  </div>
);

export default LabeledInput;
