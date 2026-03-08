import React, { useState } from 'react';
import axios from 'axios';

const QueryPlayground = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);

  const handleQuery = async () => {
    try {
      const result = await axios.post('/v1/query', { query });
      setResponse(result.data);
    } catch (error) {
      console.error('Error querying:', error);
    }
  };

  return (
    <div>
      <h1>Query Playground</h1>
      <input
        type='text'
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder='Enter your query'
      />
      <button onClick={handleQuery}>Query</button>
      {response && (
        <div>
          <h2>Answer: {response.answer}</h2>
          <h3>Sources:</h3>
          <ul>
            {response.sources.map((source, index) => (
              <li key={index}>{source.title} - {source.url}</li>
            ))}
          </ul>
          <h3>Graph Path:</h3>
          <ul>
            {response.graph_path.map((path, index) => (
              <li key={index}>{path.node} - {path.relation}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default QueryPlayground;
