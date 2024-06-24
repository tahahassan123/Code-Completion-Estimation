import React from 'react';
import { Line } from 'react-chartjs-2';
import GlobalStyle from '../../styles/GlobalStyle';
import './RiskEstimation.css';

const RiskEstimation = ({ data }) => {
  // Check if the data is provided and contains the necessary arrays
  if (!data || !data.risk_array || data.risk_array.length === 0) {
    return <p>No data available for Risk Estimation.</p>;
  }

  // Flatten the 2D array for visualization
  const flattenArray = (array) => array.flat();

  const graphData = {
    labels: data.labels || Array.from({ length: flattenArray(data.risk_array).length }, (_, i) => i + 1),
    datasets: [{
      label: 'Risk Estimation',
      data: flattenArray(data.risk_array),
      backgroundColor: 'black',
      borderColor: 'red',
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
    <div className="risk-estimation-container min-h-screen bg-background-light flex flex-col items-center justify-center p-6">
      <GlobalStyle />
      <h2>Risk Estimation</h2>
      <div className="graph-container" style={{ width: '80%', height: '400px' }}>
        <Line data={graphData} options={options} />
      </div>
      <p>Mean Risk: {data.risk_mean}</p>
    </div>
  );
};

export default RiskEstimation;
