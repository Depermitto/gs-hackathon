import '@mantine/core/styles.css';

import { Button, Title, Stack, Card, Text } from '@mantine/core';
import UploadAPI from './UploadAPI';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

function App() {
  const navigate = useNavigate();
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = (uploadedFile: File) => {
    setFile(uploadedFile);
  };

  const handleSubmit = async () => {
    if (!file) {
      alert('Please upload a file first.');
      return;
    }

    setLoading(true);
    try {
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
          <UploadAPI onUpload={handleFileUpload} />
          <Button
            size="lg"
            color="green"
            radius="xl"
            fullWidth
            onClick={handleSubmit}
            loading={loading}
            disabled={!file}
          >
            {loading ? 'Processing...' : 'Submit'}
          </Button>
        </Stack>
      </Card>
    </Stack>
  );
}

export default App;
