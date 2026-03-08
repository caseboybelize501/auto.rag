import React, { useState, useEffect } from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import axios from 'axios';

const GraphExplorer = () => {
  const [graphData, setGraphData] = useState({ nodes: [], links: [] });

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const response = await axios.get('/api/graph/nodes');
        setGraphData(response.data);
      } catch (error) {
        console.error('Error fetching graph data:', error);
      }
    };

    fetchGraphData();
  }, []);

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <ForceGraph2D
        graphData={graphData}
        nodeLabel='id'
        linkLabel='type'
      />
    </div>
  );
};

export default GraphExplorer;
