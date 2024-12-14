import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [students, setStudents] = useState([]); 

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/students')
      .then(response => {
        console.log('Backend response:', response.data); 
        setStudents(response.data);
      })
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="App">
      <h1>Students List:</h1>
      {students.length === 0 ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {students.map(student => (
            <li key={student.id}>
              <strong>{student.name}</strong> -  Media: {student.gpa}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
