import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SourceStatus = () => {
  const [sources, setSources] = useState([]);

  useEffect(() => {
    const fetchSources = async () => {
      try {
        const response = await axios.get('/api/sources');
        setSources(response.data.sources);
      } catch (error) {
        console.error('Error fetching sources:', error);
      }
    };

    fetchSources();
  }, []);

  return (
    <div>
      <h1>Source Status</h1>
      <ul>
        {sources.map(source => (
          <li key={source.source}>
            {source.source}: {source.status} - Last Synced: {source.last_synced_at}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SourceStatus;
