import React, { useState } from 'react';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const dataList = ["React", "Angular", "Vue", "Svelte", "Next.js", "Nuxt.js", "Gatsby"];

  const filteredData = dataList.filter(item =>
    item.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <h1>Search Filter</h1>
      <input 
        type="text" 
        placeholder="Search frameworks..." 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <ul>
        {filteredData.length > 0 ? (
          filteredData.map((item, index) => <li key={index}>{item}</li>)
        ) : (
          <li>No results found</li>
        )}
      </ul>
    </div>
  );
}
export default App;

