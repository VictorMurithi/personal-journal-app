// App.js

import React from 'react';
import { SafeAreaView, StyleSheet } from 'react-native';
import LoginScreen from '../screens/loginScreen';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <LoginScreen />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

export default App;
