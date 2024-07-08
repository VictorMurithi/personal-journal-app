import React from 'react';
import { TailwindProvider } from 'tailwind-rn';
import utilities from './tailwind.json';
import AppNavigator from './navigation/AppNavigator';

export default function App() {
  return (
    <TailwindProvider utilities={utilities}>
      <AppNavigator />
    </TailwindProvider>
  );
}
