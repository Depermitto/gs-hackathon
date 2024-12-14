import '@mantine/core/styles.css';

import { Button, Title, Stack, Card, Text } from '@mantine/core';
import UploadAPI from './UploadAPI';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

function App() {
  const navigate = useNavigate();
  const [file, setFile] = useState<File | null>(null);
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileUpload = (uploadedFile: File) => {
    setFile(uploadedFile);
  };

  const handleSetUrl = (url: string) => {
    setUrl(url);
  }

  const handleSubmit = async () => {
    if (!file && url === '') {
      alert('Please upload a file first.');
      return;
    }

    setLoading(true);
    try {
      if (file) {
        const formData = new FormData();
        formData.append('file', file);

      const response = await fetch('http://localhost:8000/api/process/file', {
        method: 'POST',
        body: formData,
      });

        if (!response.ok) {
          throw new Error('Failed to fetch results');
        }

        const data = await response.json();
        navigate('/results', { state: { results: data } });
      }
      else {
        const response = await fetch('http://localhost:8000/api/process/scraper', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ url }),
        });

        if (!response.ok) {
          throw new Error('Failed to fetch results');
        }

        const data = await response.json();
        navigate('/results', { state: { results: data } });
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while processing your request.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Stack align="center">
      <Title size="3rem" mt="xl" mb="l">
        BetonShield
      </Title>

      <Card shadow="md" padding="lg" radius="md" withBorder style={{ width: '60%' }}>
        <Stack align="center">
          <UploadAPI onUpload={handleFileUpload} onSetUrl={handleSetUrl} />
          <Button
            size="lg"
            color="green"
            radius="xl"
            fullWidth
            onClick={handleSubmit}
            loading={loading}
            disabled={!file && url === ''}
          >
            {loading ? 'Processing...' : 'Submit'}
          </Button>
        </Stack>
      </Card>
    </Stack>
  );
}

export default App;
