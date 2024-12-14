import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import App from './App.tsx';
import Results from './components/Results.tsx';
import { MantineProvider } from '@mantine/core';

const root = createRoot(document.getElementById('root')!);

root.render(
  <StrictMode>
    <MantineProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </BrowserRouter>
    </MantineProvider>
  </StrictMode>
);