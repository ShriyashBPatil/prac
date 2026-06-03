import React, { useState } from 'react';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const dataList = ["React", "Angular", "Vue", "Svelte", "Next.js", "Nuxt.js", "Gatsby"];

  const filteredData = dataList.filter(item =>
    item.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ padding: '20px' }}>
      <h1>Q9: Search Filter</h1>
      <input 
        type="text" 
        placeholder="Search frameworks..." 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ padding: '8px', fontSize: '16px', width: '250px' }}
      />
      <ul style={{ marginTop: '20px' }}>
        {filteredData.length > 0 ? (
          filteredData.map((item, index) => <li key={index}>{item}</li>)
        ) : (
          <li style={{ color: 'red' }}>No results found</li>
        )}
      </ul>
    </div>
  );
}
export default App;
