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
    <div>
      <h1>Q10: To-Do List</h1>
      <div>
        <input 
          type="text" 
          value={taskText} 
          onChange={(e) => setTaskText(e.target.value)} 
          placeholder="New task..."
        />
        <button onClick={addTask}>Add</button>
      </div>
      
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <span onClick={() => toggleTask(task.id)}>
              {task.completed ? "[X]" : "[ ]"} {task.text}
            </span>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default App;
