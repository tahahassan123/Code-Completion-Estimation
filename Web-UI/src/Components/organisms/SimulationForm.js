import React, { useState } from 'react';
import LabeledInput from '../molecules/LabeledInput';
import Button from '../atoms/Button';

const SimulationForm = ({ runSimulation }) => {
  const [minTime, setMinTime] = useState('');
  const [maxTime, setMaxTime] = useState('');
  const [minLOC, setMinLOC] = useState('');
  const [maxLOC, setMaxLOC] = useState('');
  const [minFP, setMinFP] = useState('');
  const [maxFP, setMaxFP] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    runSimulation({ minTime, maxTime, minLOC, maxLOC, minFP, maxFP });
  };

  return (
    <form onSubmit={handleSubmit}>
      <LabeledInput label="Min Time" type="number" value={minTime} onChange={(e) => setMinTime(e.target.value)} />
      <LabeledInput label="Max Time" type="number" value={maxTime} onChange={(e) => setMaxTime(e.target.value)} />
      <LabeledInput label="Min LOC" type="number" value={minLOC} onChange={(e) => setMinLOC(e.target.value)} />
      <LabeledInput label="Max LOC" type="number" value={maxLOC} onChange={(e) => setMaxLOC(e.target.value)} />
      <LabeledInput label="Min Functional Points" type="number" value={minFP} onChange={(e) => setMinFP(e.target.value)} />
      <LabeledInput label="Max Functional Points" type="number" value={maxFP} onChange={(e) => setMaxFP(e.target.value)} />
      <Button type="submit">Run Simulation</Button>
    </form>
  );
};

export default SimulationForm;