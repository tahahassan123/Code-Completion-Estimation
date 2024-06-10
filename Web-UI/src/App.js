import React, { useState, useEffect } from 'react';
import { useSpring, useTransition, animated } from '@react-spring/web';
import MonteCarloSimulation from './Components/pages/MonteCarloSimulation';
import GlobalStyle from './styles/GlobalStyle';
import Button from './Components/atoms/Button'; 
import './App.css';
const images = [
  'https://resources.scrumalliance.org/uploads/2021/9/27/Math%201200x630-h9GdzifxMEiJt6cU9UXT8w.jpg',
  'https://www.simplilearn.com/ice9/free_resources_article_thumb/estimation-tools-and-techniques-part-i-article.jpg',
  'https://cdn.prod.website-files.com/65ecef8ade5270cf83291da8/662af171884bff4abb6d010e_Estimating%20methodologies-p-800.png',
];


function App() {
  const [showSimulation, setShowSimulation] = useState(false);
  const [index, setIndex] = useState(0);
  const [results, setResults] = useState(null);

  const fadeIn = useSpring({
    opacity: showSimulation ? 1 : 0,
    transform: showSimulation ? 'translateY(0)' : 'translateY(-20px)',
  });

  const transitions = useTransition(index, {
    from: { opacity: 0, transform: 'translateX(100%)' },
    enter: { opacity: 1, transform: 'translateX(0%)' },
    leave: { opacity: 0, transform: 'translateX(-100%)' },
    config: { duration: 1000 },
  });

  const handleStart = () => {
    setShowSimulation(true);
  };

  const runSimulation = async (data) => {
    try {
      const response = await fetch('https://your-backend-endpoint/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      setResults(result);
    } catch (error) {
      console.error('Error running simulation:', error);
      alert('An error occurred while running the simulation. Please try again.');
    }
  };

  useEffect(() => {
    if (!showSimulation) return;
    const interval = setInterval(() => {
      setIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 3000);
    return () => clearInterval(interval);
  }, [showSimulation]);

  return (
    <div className="min-h-screen bg-background-light flex flex-col items-center justify-center p-6">
      <GlobalStyle />
      <div className="text-center">
        <h1 className="text-4xl font-bold text-primary-dark mb-4">Code Estimator</h1>
        <p className="text-lg text-secondary mb-6">Estimate coding timelines and effort complexity using Monte Carlo simulations.</p>
        {!showSimulation && (
          <Button onClick={handleStart}>
            Start Estimation
          </Button>
        )}
      </div>
      {showSimulation && (
        <>
          <div className="relative w-full h-64 mt-6 overflow-hidden rounded-lg">
            {transitions((style, i) => (
              <animated.div
                key={i}
                style={{ ...style, backgroundImage: `url(${images[i]})` }}
                className="absolute w-full h-full bg-center bg-cover"
              />
            ))}
          </div>
          <animated.div style={fadeIn} className="w-full mt-6">
            <MonteCarloSimulation runSimulation={runSimulation} results={results} />
          </animated.div>
        </>
      )}
    </div>
  );
}

export default App;