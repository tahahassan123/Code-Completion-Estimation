import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    font-family: 'Arial', sans-serif;
    background: linear-gradient(45deg, #37474f, #b0bec5);
    background-size: 200% 200%;
    animation: backgroundShift 10s ease infinite, backgroundTransition 10s infinite alternate;
  }

  @keyframes backgroundShift {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }

  @keyframes backgroundTransition {
    0% {
      background-color: #37474f;
    }
    100% {
      background-color: #ffffff;
    }
  }

  .bg-metallic {
    background: linear-gradient(45deg, #c0c0c0, #808080);
    background-size: 200% 200%;
    animation: backgroundShift 10s ease infinite, backgroundTransition 10s infinite alternate;
  }

  .text-metallic {
    color: #292108;
  }
`;

export default GlobalStyle;
