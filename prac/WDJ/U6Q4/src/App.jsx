import React, { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  const handleClick = () => {
    setMessage('Button was clicked!');
  };

  const handleMouseOver = () => {
    setMessage('Mouse is hovering over the area!');
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Q4: Event Handling</h1>
      <button onClick={handleClick}>Click Me</button>
      <div 
        onMouseOver={handleMouseOver} 
        style={{ marginTop: '20px', padding: '20px', backgroundColor: '#f0f0f0', border: '1px dashed #333', cursor: 'pointer' }}
      >
        Hover over me!
      </div>
      <h3 style={{ color: 'blue' }}>{message}</h3>
    </div>
  );
}
export default App;
