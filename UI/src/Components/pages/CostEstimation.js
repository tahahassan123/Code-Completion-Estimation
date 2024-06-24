import React from 'react';
import { Line } from 'react-chartjs-2';
import GlobalStyle from '../../styles/GlobalStyle';
import './LOCestimation.css';

const CostEstimation = ({ data }) => {
  // Check if the data is provided and contains the necessary arrays
  if (!data || !data.cost_array || data.cost_array.length === 0) {
    return <p>No data available for Cost Estimation.</p>;
  }

  // Flatten the 2D array for visualization
  const flattenArray = (array) => array.flat();

  const graphData = {
    labels: data.labels || Array.from({ length: flattenArray(data.cost_array).length }, (_, i) => i + 1),
    datasets: [{
      label: 'Cost Estimation',
      data: flattenArray(data.cost_array),
      backgroundColor: 'black',
      borderColor: 'white',
      borderWidth: 1.5
    }]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        beginAtZero: true,
        ticks: {
          font: {
            size: 20,
            weight: 'bold',
            family: 'Arial',
            color: '#FFFFFF' // Vibrant color for x-axis labels
          }
        }
      },
      y: {
        beginAtZero: true,
        ticks: {
          font: {
            size: 20,
            weight: 'bold',
            family: 'Arial',
            color: '#FFFFFF' // Vibrant color for y-axis labels
          }
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          font: {
            size: 20,
            weight: 'bold',
            family: 'Arial',
            color: '#FFFFFF' // Vibrant color for legend labels
          }
        }
      }
    }
  };

  return (
    <div className="cost-estimation-container min-h-screen bg-background-light flex flex-col items-center justify-center p-6">
      <GlobalStyle />
      <h2>Cost Estimation</h2>
      <div className="graph-container" style={{ width: '80%', height: '400px' }}>
        <Line data={graphData} options={options} />
      </div>
      <p>Estimated Cost: ${data.cost_mean}</p>
    </div>
  );
};

export default CostEstimation;
