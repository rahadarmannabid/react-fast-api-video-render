// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import './App.css';

// function App() {
//   const [people, setPeople] = useState([]);
//   const [newPerson, setNewPerson] = useState("");

//   useEffect(() => {
//     axios.get('http://localhost:8000/api/')
//          .then(response => setPeople(response.data))
//          .catch(error => console.error('Error fetching data:', error));
//   }, [people]); // Adding people as a dependency

//   const addPerson = () => {
//     axios.post('http://localhost:8000/api/add', { name: newPerson })
//          .then(response => {
//            setPeople([...people, { name: newPerson }]);
//            setNewPerson("");
//          })
//          .catch(error => console.error('Error adding person:', error));
//   };

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>People</h1>
//         <div>
//           <input 
//             type="text" 
//             value={newPerson} 
//             onChange={e => setNewPerson(e.target.value)} 
//             placeholder="Enter name"
//           />
//           <button onClick={addPerson}>Add Person</button>
//         </div>
//         {people.map((person, index) => (
//           <p key={index}>{person.name}</p>
//         ))}
//       </header>
//     </div>
//   );
// }

// export default App;


import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [videoUrl, setVideoUrl] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/video')
         .then(response => {
           setVideoUrl(response.data.url);
         })
         .catch(error => console.error('Error fetching video URL:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Video from Backend</h1>
        {videoUrl && (
          <iframe
            width="560"
            height="315"
            src={`https://www.youtube.com/embed/${videoUrl.split('v=')[1]}`}
            title="YouTube video player"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen>
          </iframe>
        )}
      </header>
    </div>
  );
}

export default App;
