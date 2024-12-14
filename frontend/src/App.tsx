import '@mantine/core/styles.css'

import { Box, Button, Title } from '@mantine/core';
import UploadAPI from './UploadAPI';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

function App() {
  const navigate = useNavigate();
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  
  const handleFileUpload = (uploadedFile: File) => {
    setFile(uploadedFile);
  }

  const handleSubmit = async () => {
    if (!file) {
      alert('Please upload a file first.');
      return;
    }
  
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append('file', file);

      // Make the API request
      const response = await fetch('http://localhost:8000/api/process', {
        method: 'POST',
        body: formData, // Example payload
      });

      if (!response.ok) {
        throw new Error('Failed to fetch results');
      }

      const data = await response.json();

      // Redirect to the results page and pass the data (or a reference)
      navigate('/results', { state: { results: data } });
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while processing your request.');
    } finally {
      setLoading(false);
    }
  }


  return (
      <Box>
        <Title className="text-center">BetonShield</Title>
        <UploadAPI onUpload={handleFileUpload} />
        <Box className='text-center m-auto w-1/2 max-w-96'>
          <Button fullWidth color='green' onClick={handleSubmit} loading={loading}>Submit</Button>
        </Box>
      </Box>
  )
}

export default App;
