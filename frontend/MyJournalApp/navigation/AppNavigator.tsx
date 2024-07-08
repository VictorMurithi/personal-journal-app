import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from '../screens/loginScreen';

const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <>
      <Stack.Navigator>
        <Stack.Screen name="login" component={LoginScreen} />
      </Stack.Navigator>
    </>
  );
};

export default AppNavigator;
