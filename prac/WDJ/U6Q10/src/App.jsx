import React, { useState } from 'react';

function App() {
  const [tasks, setTasks] = useState([]);
  const [taskText, setTaskText] = useState('');

  const addTask = () => {
    if (taskText.trim() !== '') {
      setTasks([...tasks, { id: Date.now(), text: taskText, completed: false }]);
      setTaskText('');
    }
  };

  const toggleTask = (id) => {
    setTasks(tasks.map(task => 
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px' }}>
      <h1>Q10: To-Do List</h1>
      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input 
          type="text" 
          value={taskText} 
          onChange={(e) => setTaskText(e.target.value)} 
          placeholder="New task..."
          style={{ flex: 1, padding: '8px' }}
        />
        <button onClick={addTask} style={{ padding: '8px 15px' }}>Add</button>
      </div>
      
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {tasks.map(task => (
          <li key={task.id} style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px', padding: '10px', border: '1px solid #ddd' }}>
            <span 
              onClick={() => toggleTask(task.id)}
              style={{ textDecoration: task.completed ? 'line-through' : 'none', cursor: 'pointer', flex: 1 }}
            >
              {task.text}
            </span>
            <button onClick={() => deleteTask(task.id)} style={{ color: 'red', border: 'none', background: 'none', cursor: 'pointer' }}>X</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default App;
