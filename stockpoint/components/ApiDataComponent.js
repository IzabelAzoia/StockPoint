import React from 'react';
import { SafeAreaView, StyleSheet } from 'react-native';
import ApiDataComponent from './ApiDataComponent';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <ApiDataComponent />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});

export default App;

