import React from 'react';
import SimulationForm from '../organisms/SimulationForm';

const MonteCarloSimulation = ({ runSimulation, results }) => (
  <div className="p-6 max-w-4xl mx-auto bg-background rounded-lg shadow-lg">
    <SimulationForm runSimulation={runSimulation} />
    {results && (
      <div className="mt-6">
        <h2 className="text-xl font-bold text-primary-dark">Results</h2>
        <img src={results.graphUrl} alt="Simulation Graph" className="w-full mt-4 rounded-lg" />
        <div className="mt-4">
          <p>{results.summary}</p>
        </div>
      </div>
    )}
  </div>
);

export default MonteCarloSimulation;