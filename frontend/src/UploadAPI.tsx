import { useRef, useState } from 'react';
import { Text, Button, Stack, Center, TextInput } from '@mantine/core';
import { Dropzone } from '@mantine/dropzone';

function UploadAPI(props: { onUpload: (file: File) => void }) {
    const { onUpload } = props;
    const openRef = useRef<() => void>(null);
    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    const onAddFile = (files: File[]) => {
        if (files.length > 0) {
            setSelectedFile(files[0]);
            onUpload(files[0]);
        }
    }

    return (
        <Stack align="center">
            <Text size="lg">
            Upload the documentation file
            </Text>

            <TextInput
                placeholder="https://api.example.com/docs"
                label="Enter the API documentation URL below:"
                radius="md"
                size="md"
                style={{ width: '100%' }}
            />

            <Text>
                Or drag and drop a YAML file into the area below, or click to select a file manually.
            </Text>

            <Dropzone
            openRef={openRef}
            onDrop={onAddFile}
            accept={['application/yaml']}
            styles={{
                root: {
                borderWidth: '2px',
                borderStyle: 'dashed',
                borderRadius: '8px',
                padding: '40px',
                backgroundColor: '#f8fafc',
                },
            }}
            >
                <Center>
                    <Dropzone.Idle>
                    <Center>
                        <Button mb="lg" variant="outline" radius="xl" onClick={() => openRef.current?.()}>
                            Select File
                        </Button>
                    </Center>
                    <Text size="sm" c="dimmed">
                        Supported formats: YAML
                    </Text>
                    </Dropzone.Idle>
                    <Dropzone.Accept>
                    <Text c="green" size="sm">
                        Drop the file here to upload
                    </Text>
                    </Dropzone.Accept>
                    <Dropzone.Reject>
                    <Text c="red" size="sm">
                        Unsupported file type
                    </Text>
                    </Dropzone.Reject>
                </Center>
            </Dropzone>

            <Text size="xs" c="dimmed">
                Tip: You can drag and drop files here!
            </Text>

            {selectedFile && (
            <Text size="sm" c="green">
                Selected file: <strong>{selectedFile.name}</strong>
            </Text>
            )}
      </Stack>
    )
}

export default UploadAPI