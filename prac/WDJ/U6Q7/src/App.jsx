import React, { useState } from 'react';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div>
      <h1>Q7: Conditional Rendering</h1>
      {isLoggedIn ? (
        <div>
          <h2>Welcome back, User!</h2>
          <button onClick={() => setIsLoggedIn(false)}>Logout</button>
        </div>
      ) : (
        <div>
          <h2>Please log in to continue.</h2>
          <button onClick={() => setIsLoggedIn(true)}>Login</button>
        </div>
      )}
    </div>
  );
}
export default App;
