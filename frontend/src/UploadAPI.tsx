import { useRef, useState } from 'react';
import { Text, Button, Group } from '@mantine/core';
import { Dropzone } from '@mantine/dropzone';

function UploadAPI(props: { onUpload: (file: File) => void }) {
    const { onUpload } = props;
    const openRef = useRef<() => void>(null);
    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    const onAddFile = (files: File[]) => {
        if (files.length > 0) {
            console.log(files);
            setSelectedFile(files[0]);
            onUpload(files[0]);
        }
    }

    return (
        <div className="text-center m-auto w-1/2 max-w-96">
            {/* <p>Enter the API documentation URL below:</p>
            <TextInput className="py-2" placeholder="https://api.example.com/docs" />
            <p>Or upload the documentation file</p> */}
            <Text>Upload the documentation file:</Text>
            <Dropzone
                className="border-dashed border-2 rounded-md py-10"
                openRef={openRef}
                accept={['application/json', 'application/yaml']}
                onDrop={onAddFile}
            >
                <Group justify='center'>
                    <Dropzone.Idle>
                        <Button onClick={() => openRef.current?.()} style={{ pointerEvents: 'all' }}>
                            Select file
                        </Button>
                    </Dropzone.Idle>
                    <Dropzone.Accept>
                        Release the mouse button to upload the file
                    </Dropzone.Accept>
                    <Dropzone.Reject>
                        <Button onClick={() => openRef.current?.()} style={{ pointerEvents: 'all' }}>
                            Select files
                        </Button>
                        <Text>File type not supported (only JSON and YAML files are accepted)</Text>
                    </Dropzone.Reject>
                </Group>
            </Dropzone> 
            <p className='py-2 text-xs text-gray-500 text-center'>Pro-tip: you can also drag and drop files in the area above!</p>
            {selectedFile && (
                <p className="py-2 text-green-500 text-center">
                    Selected file: {selectedFile.name}
                </p>
            )}
        </div>
    )
}

export default UploadAPI