import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { useSpring, animated } from '@react-spring/web';
import GlobalStyle from './styles/GlobalStyle';
import Button from './Components/atoms/Button';
import LOCestimation from './Components/pages/LOCestimation';
import ComplexityEstimation from './Components/pages/ComplexityEstimation';
import DevelopmentTimeEstimation from './Components/pages/DevelopmentTimeEstimation';
import CostEstimation from './Components/pages/CostEstimation';
import NumberOfPeopleEstimation from './Components/pages/NumberOfPeopleEstimation';
import CodeCoverageEstimation from './Components/pages/CodeCoverageEstimation';
import RiskEstimation from './Components/pages/RiskEstimation';
import SimulationForm from './Components/organisms/SimulationForm';
import './App.css';
import './chartSetup'; // Import the chart setup file

const images = [
  'https://resources.scrumalliance.org/uploads/2021/9/27/Math%201200x630-h9GdzifxMEiJt6cU9UXT8w.jpg',
  'https://media.istockphoto.com/id/1669453534/photo/3d-render-cloud-computing-circuit-board-background.jpg?s=2048x2048&w=is&k=20&c=01KGhosLc5DFL0QPh0_lUaMUtq6BtSAmodICfv_CdNE=',
  'https://media.istockphoto.com/id/537331500/photo/programming-code-abstract-technology-background-of-software-deve.webp?s=2048x2048&w=is&k=20&c=QmU65ppziekU7cl_KNWyMCteKvhhSYueIqEBlQWvid0=',
  'https://www.simplilearn.com/ice9/free_resources_article_thumb/estimation-tools-and-techniques-part-i-article.jpg',
  'https://cdn.prod.website-files.com/65ecef8ade5270cf83291da8/662af171884bff4abb6d010e_Estimating%20methodologies-p-800.png',
  'https://img.pikbest.com/origin/09/43/34/85EpIkbEsTNYi.jpg!w700wp',
];

function App() {
  const [showSimulation, setShowSimulation] = useState(false);
  const [index, setIndex] = useState(0);
  const [results, setResults] = useState(null);

  const fadeIn = useSpring({
    opacity: showSimulation ? 1 : 0,
    transform: showSimulation ? 'translateY(0)' : 'translateY(-20px)',
  });

  const handleStart = () => {
    setShowSimulation(true);
  };

  const runSimulation = (data) => {
    setResults(data);
  };

  useEffect(() => {
    if (!showSimulation) return;
    const interval = setInterval(() => {
      setIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 3000);
    return () => clearInterval(interval);
  }, [showSimulation]);


  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-r from-gray-800 to-gray-700 animate-gradient-x flex flex-col items-center justify-center p-6">
        <GlobalStyle />
        <div className="text-center">
          <h1 className="text-4xl font-bold text-white mb-4">Code Estimator</h1>
          <p className="text-lg text-gray-300 mb-6">Estimate coding timelines and effort complexity using Monte Carlo simulations.</p>
          {!showSimulation && (
            <Button onClick={handleStart}>
              Start Estimation
            </Button>
          )}
        </div>
        {showSimulation && (
           <>
           <div className="relative w-full h-64 mt-6 overflow-hidden rounded-lg shadow-md border border-gray-700">
             {images.map((imageUrl, i) => (
               <animated.div
                 key={i}
                 style={{
                   opacity: index === i ? 1 : 0,
                   backgroundImage: `url(${imageUrl})`,
                 }}
                 className={`absolute w-full h-full bg-center bg-cover transition-opacity duration-1000`}
               />
             ))}
           </div>
            <animated.div style={fadeIn} className="w-full mt-6">
              <Routes>
                <Route path="/" element={<SimulationForm runSimulation={runSimulation} />} />
                <Route path="/loc-estimation" element={<LOCestimation data={results} />} />
                <Route path="/complexity-estimation" element={<ComplexityEstimation data={results} />} />
                <Route path="/development-time-estimation" element={<DevelopmentTimeEstimation data={results} />} />
                <Route path="/cost-estimation" element={<CostEstimation data={results} />} />
                <Route path="/number-people-estimation" element={<NumberOfPeopleEstimation data={results} />} />
                <Route path="/code-coverage" element={<CodeCoverageEstimation data={results} />} />
                <Route path="/risk-estimation" element={<RiskEstimation data={results} />} />
              </Routes>
            </animated.div>
            <div className="mt-6 flex space-x-4">
              <Link to="/loc-estimation" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Go to LOC Estimation
              </Link>
              <Link to="/complexity-estimation" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Go to Complexity Estimation
              </Link>
              <Link to="/development-time-estimation" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Development Time Estimation
              </Link>
              <Link to="/cost-estimation" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Cost Estimation
              </Link>
              <Link to="/number-people-estimation" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Number of People Estimation
              </Link>
              <Link to="/code-coverage" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Code Coverage Estimation
              </Link>
              <Link to="/risk-estimation" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Risk Estimation
              </Link>
              <Link to="/" className="metallic-link text-white font-bold py-2 px-4 rounded transition duration-300">
                Go Back
              </Link>
            </div>
          </>
        )}
      </div>
    </Router>
  );
}

export default App;
