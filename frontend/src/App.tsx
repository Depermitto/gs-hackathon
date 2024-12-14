import '@mantine/core/styles.css'

import { Button, MantineProvider } from '@mantine/core';
import UploadAPI from './UploadAPI';

function App() {
  return (
    <MantineProvider>
      <>
      <h1 className="text-4xl font-mono text-center">BetonShield</h1>
      <UploadAPI />
      <div className='text-center m-auto w-1/2 max-w-96'>
        <Button fullWidth color='green'>Submit</Button>
      </div>
      </>
    </MantineProvider>
  )
}

export default App;
