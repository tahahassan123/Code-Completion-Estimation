import React, { useState } from 'react';

const MonteCarloSimulation = ({ runSimulation, results }) => {
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
    <div className="p-6 max-w-4xl mx-auto bg-background rounded-lg shadow-lg">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Min Time</label>
          <input
            type="number"
            value={minTime}
            onChange={(e) => setMinTime(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Max Time</label>
          <input
            type="number"
            value={maxTime}
            onChange={(e) => setMaxTime(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Min LOC</label>
          <input
            type="number"
            value={minLOC}
            onChange={(e) => setMinLOC(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Max LOC</label>
          <input
            type="number"
            value={maxLOC}
            onChange={(e) => setMaxLOC(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Min Functional Points</label>
          <input
            type="number"
            value={minFP}
            onChange={(e) => setMinFP(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Max Functional Points</label>
          <input
            type="number"
            value={maxFP}
            onChange={(e) => setMaxFP(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            required
          />
        </div>
        <button
          type="submit"
          className="bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4 rounded transition duration-300"
        >
          Run Simulation
        </button>
      </form>
      {results && (
        <div className="mt-6">
          <h2 className="text-xl font-bold text-primary-dark">Results</h2>
          {/* Assuming results contain a graph URL */}
          <img src={results.graphUrl} alt="Simulation Graph" className="w-full mt-4 rounded-lg" />
          <div className="mt-4">
            {/* Additional results display */}
            <p>{results.summary}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default MonteCarloSimulation;
