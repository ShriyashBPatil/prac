import React from 'react';

function StudentInfo(props) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', width: '250px', marginBottom: '10px' }}>
      <h3>Student Details</h3>
      <p><strong>Name:</strong> {props.name}</p>
      <p><strong>Roll No:</strong> {props.roll}</p>
      <p><strong>Course:</strong> {props.course}</p>
    </div>
  );
}

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Q3: Props in React</h1>
      <StudentInfo name="John Doe" roll="101" course="B.Sc IT" />
      <StudentInfo name="Jane Smith" roll="102" course="BCA" />
    </div>
  );
}
export default App;
