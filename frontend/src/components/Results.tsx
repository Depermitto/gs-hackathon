import '@mantine/core/styles.css'

import { Title } from '@mantine/core';
import { useLocation } from 'react-router-dom';

function Results() {
  const location = useLocation();
  const results = location.state?.results;
    
  return (
      <>
      <Title className="text-center">BetonShield</Title>
      {results ? (
          <div className="text-center m-auto w-1/2 max-w-96">
            <p>{results.errors.message}: {results.errors.code}</p>
          </div>
        ) : (
            <p>Something went wrong!</p>
        )}
      </>
  )
}

export default Results;
