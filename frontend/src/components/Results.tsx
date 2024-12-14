import '@mantine/core/styles.css'

import { Title, Text, Stack, Group, Button, Table } from '@mantine/core';
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
              : 'No vulnerabilities found!'
            }
          </Text>
          {results.vulnerabilities && (
              <Table>
                <Table.Thead>
                  <Table.Tr>
                    <Table.Th>Type</Table.Th>
                    <Table.Th>Description</Table.Th>
                  </Table.Tr>
                </Table.Thead>
                <Table.Tbody>
                  {results.https == false && (
                    <Table.Tr>
                      <Table.Td>HTTPS</Table.Td>
                      <Table.Td>HTTPS protocol is not used</Table.Td>
                    </Table.Tr>
                  )}
                  {results.cookie_permanent == true && (
                    <Table.Tr>
                      <Table.Td>Cookie</Table.Td>
                      <Table.Td>Cookie does not have the Secure and HttpOnly flags set</Table.Td>
                    </Table.Tr>
                  )}
                  {results.cookie_secure == false && (
                    <Table.Tr>
                      <Table.Td>Cookie</Table.Td>
                      <Table.Td>Cookie does not have the Secure flag set</Table.Td>
                    </Table.Tr>
                  )}
                  {results.sql && results.sql.map((item: any, index: any) => (
                    <>
                      {item.body_injection && (
                        <Table.Tr key={`body-${index}`}>
                          <Table.Td>{item.route}</Table.Td>
                          <Table.Td>Body injection vulnerability detected</Table.Td>
                        </Table.Tr>
                      )}
                      {item.path_injection && (
                        <Table.Tr key={`path-${index}`}>
                          <Table.Td>{item.route}</Table.Td>
                          <Table.Td>Path injection vulnerability detected</Table.Td>
                        </Table.Tr>
                      )}
                    </>
                  ))}
                </Table.Tbody>
              </Table>
          )}
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
