import React from 'react';

function App() {
  const fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Orange'];

  return (
    <div>
      <h1>Q6: Lists using Array Mapping</h1>
      <ul>
        {fruits.map((fruit, index) => (
          <li key={index}>{fruit}</li>
        ))}
      </ul>
    </div>
  );
}
export default App;
