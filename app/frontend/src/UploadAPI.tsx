import { useRef } from 'react';
import { TextInput, Button, Group } from '@mantine/core';
import { Dropzone } from '@mantine/dropzone';

function UploadAPI() {
    const openRef = useRef<() => void>(null);

    return (
        <div className="text-center m-auto w-1/2 max-w-96">
            <p>Enter the API documentation URL below:</p>
            <TextInput className="py-2" placeholder="https://api.example.com/docs" />
            <p>Or upload the documentation file</p>
            <Dropzone className="border-dashed border-2 rounded-md py-10" openRef={openRef} accept={['application/json', 'application/yaml']} onDrop={() => {}} activateOnClick={false}>{
                <Group justify='center'>
                    <Dropzone.Idle>
                        <Button onClick={() => openRef.current?.()} style={{ pointerEvents: 'all' }}>
                            Select files
                        </Button>
                    </Dropzone.Idle>
                    <Dropzone.Accept>
                        Release the mouse button to upload the file
                    </Dropzone.Accept>
                    <Dropzone.Reject>
                        File type not supported (only JSON and YAML files are accepted)
                    </Dropzone.Reject>
                </Group>
            }</Dropzone> 
            <p className='py-2 text-xs text-gray-500 text-center'>Pro tip: you can also drag and drop files in the area above!</p>
        </div>
    )
}

export default UploadAPI