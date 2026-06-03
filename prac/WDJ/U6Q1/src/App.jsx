import React from 'react';

function Greeting() {
  return <h2>Hello, welcome to React!</h2>;
}

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Q1: Components and JSX</h1>
      <Greeting />
    </div>
  );
}
export default App;
