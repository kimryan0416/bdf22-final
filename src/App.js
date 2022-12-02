import { useState, useEffect } from "react";
import './App.css';
import { Map } from './components';

const url = 'https://opendata.arcgis.com/datasets/c35786feb0ac4d1b964f41f874f151c1_0.geojson';

function App() {

  const [data, setData] = useState();

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(res => setData(res));
  });

  return (
    <div className="App">
      <Map geoJson={data} />
    </div>
  );
}

export default App;
