import '@mantine/core/styles.css'

import { Title, Text, Stack, Group, Button } from '@mantine/core';
import { useLocation, useNavigate } from 'react-router-dom';
import { IconCircleCheck, IconCircleX } from '@tabler/icons-react';

function Results() {
  const location = useLocation();
  const results = location.state?.results;
  const navigate = useNavigate();

  const handleGoBack = () => {
    navigate('/');
  };

  console.log(results);
  return (
    <Stack align="center">
      <Title order={1} size="3rem" mt="xl" mb="l">
        BetonShield
      </Title>

      {results ? (
        <Stack align="center">
          {results.vulnerabilities ? (
            <IconCircleX size={72} color="red" />
          ) : (
            <IconCircleCheck size={72} color="green" />
          )}
          <Text size="lg">
            {results.vulnerabilities
              ? `Found vulnerabilities: ${results.vulnerabilities}`
              : 'No vulnerabilities found!'}
          </Text>
        </Stack>
      ) : (
        <Text size="lg" c="red">
          Something went wrong!
        </Text>
      )}

      <Group>
        <Button size="md" radius="xl" variant="outline" color="blue" onClick={handleGoBack}>
          Go Back
        </Button>
      </Group>
    </Stack>
  )
}

export default Results;
