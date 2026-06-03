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
    <div>
      <h1>Event Handling</h1>
      <button onClick={handleClick}>Click Me</button>
      <div onMouseOver={handleMouseOver}>
        <br/>Hover over me!<br/>
      </div>
      <h3>{message}</h3>
    </div>
  );
}
export default App;

