import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';
import LoginScreen from '@/screens/loginScreen';
import SignupScreen from '@/screens/signupScreen';
import JournalScreen from '@/screens/JournalScreen';
import SettingsScreen from '@/screens/SettingsScreen';
import SummaryScreen from '@/screens/SettingsScreen';

const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <>
      <Stack.Navigator>
        <Stack.Screen name="login" component={LoginScreen} />
        <Stack.Screen name="signup" component={SignupScreen} />
        <Stack.Screen name="journal" component={JournalScreen} />
        <Stack.Screen name="settings" component={SettingsScreen} />
        <Stack.Screen name="summary" component={SummaryScreen} />
      </Stack.Navigator>
    </>
  );
};

export default AppNavigator;
