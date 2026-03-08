import React, { useState } from 'react';
import axios from 'axios';

const EntitySearch = () => {
  const [query, setQuery] = useState('');
  const [entities, setEntities] = useState([]);

  const handleSearch = async () => {
    try {
      const result = await axios.get('/api/entities/search', { params: { q: query } });
      setEntities(result.data.entities);
    } catch (error) {
      console.error('Error searching entities:', error);
    }
  };

  return (
    <div>
      <h1>Entity Search</h1>
      <input
        type='text'
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder='Search entities'
      />
      <button onClick={handleSearch}>Search</button>
      <ul>
        {entities.map(entity => (
          <li key={entity.id}>{entity.name} - {entity.type}</li>
        ))}
      </ul>
    </div>
  );
};

export default EntitySearch;
