import React from 'react';

function App() {
  const fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Orange'];

  return (
    <div style={{ padding: '20px' }}>
      <h1>Q6: Lists using Array Mapping</h1>
      <ul>
        {fruits.map((fruit, index) => (
          <li key={index} style={{ fontSize: '18px', margin: '5px 0' }}>{fruit}</li>
        ))}
      </ul>
    </div>
  );
}
export default App;
