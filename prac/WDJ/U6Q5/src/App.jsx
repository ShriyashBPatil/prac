import React, { useState, useEffect } from 'react';

function App() {
  const [formData, setFormData] = useState({ name: '', email: '' });
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    if (submitted) {
      console.log('Form submitted successfully:', formData);
      alert('Form submitted! Check console.');
      setSubmitted(false);
    }
  }, [submitted, formData]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div>
      <h1>Forms with useState & useEffect</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name: </label>
          <input type="text" name="name" value={formData.name} onChange={handleChange} required />
        </div>
        <div>
          <label>Email: </label>
          <input type="email" name="email" value={formData.email} onChange={handleChange} required />
        </div>
        <button type="submit">Submit</button>
      </form>
      <div>
        <strong>Current Input:</strong> {formData.name} ({formData.email})
      </div>
    </div>
  );
}
export default App;

