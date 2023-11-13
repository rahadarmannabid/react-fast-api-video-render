import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [videoUrl, setVideoUrl] = useState('');
  const [videoData, setVideoData] = useState(null);

  const fetchVideoData = () => {
    axios.post('http://localhost:8000/api/video', { url: videoUrl })
         .then(response => {
           setVideoData(response.data);
         })
         .catch(error => console.error('Error fetching video data:', error));
  };

  return (
    <div className="App">
      <header className="App-header">
        <input 
          type="text" 
          value={videoUrl} 
          onChange={(e) => setVideoUrl(e.target.value)}
          placeholder="Paste YouTube URL here"
        />
        <button onClick={fetchVideoData}>Load Video</button>
        {videoData && (
          <>
            <iframe
              width="560"
              height="315"
              src={`https://www.youtube.com/embed/${videoData.url.split('v=')[1]}`}
              title="YouTube video player"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen>
            </iframe>
            <p>{videoData.transcript}</p>
          </>
        )}
      </header>
    </div>
  );
}

export default App;
