import { useRef, useEffect } from 'react';
import * as d3 from 'd3';

export const Map = (props) => {

  const { geoJson } = props;

  const svgRef = useRef();

  const renderMap = (mapData, path) => {

  	const maxPrecincts = mapData.features.reduce((accumulator,next)=>{
  		if (next.properties["Precinct"] > accumulator) accumulator = next.properties["Precinct"];
  		return accumulator;
  	},0);

  	var myColor = d3.scaleLinear().domain([1,maxPrecincts]).range(["yellow", "blue"]);

    d3.select(svgRef.current)
      .selectAll('path')
      .data(mapData.features)
      .enter()
      .append('path')
      .attr('id', d => `precinct-${d.properties['Precinct']}`)
      .attr('d', path)
      .attr('stroke', '#000000')
      .attr('stroke-width', '.2')
      .attr('fill', d => myColor(d.properties['Precinct']));
  }

  useEffect(() => {
    const height = svgRef.current.clientHeight;
    const width = svgRef.current.clientWidth;
    const projection = d3.geoAlbers().fitSize([height, width], geoJson);
	const pathGenerator = d3.geoPath().projection(projection);
    if (geoJson) {
      renderMap(geoJson, pathGenerator);
    }
  }, [geoJson]);

  return (
    <div className='wrapper'>
      <svg 
        className='precincts-map' 
        ref={svgRef} 
        height={500} 
        width={500}
        style={{marginTop: '2em'}}
      />
    </div>
  );
}