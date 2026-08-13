import '@skyscanner/backpack-web/bpk-stylesheets/base';
import '@skyscanner/backpack-web/bpk-stylesheets/base.css';
import '@skyscanner/backpack-web/bpk-stylesheets/font';
import '@skyscanner/backpack-web/bpk-stylesheets/font.css';

import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);

