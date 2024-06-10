import React from 'react';
import Input from '../atoms/Input';

const LabeledInput = ({ label, value, onChange, type = 'text' }) => (
  <div className="mb-4">
    <label className="block text-sm font-medium text-gray-700">{label}</label>
    <Input type={type} value={value} onChange={onChange} />
  </div>
);

export default LabeledInput;