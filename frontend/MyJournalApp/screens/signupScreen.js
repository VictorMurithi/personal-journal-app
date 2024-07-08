import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { useTailwind } from 'tailwind-rn';

const SignupScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const tailwind = useTailwind();

  const handleSignup = async () => {
    try {
      const response = await fetch('http://your-backend-url/sign-up', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
      });

      const data = await response.json();
      if (response.ok) {
        if (data.access_token) {
          navigation.navigate('Main');
        } else {
          alert('Signup failed');
        }
      } else {
        alert('Signup failed');
      }
    } catch (error) {
      console.error(error);
      alert('An error occurred');
    }
  };

  return (
    <View style={tailwind('flex-1 p-4 justify-center')}>
      <Text style={tailwind('mb-2')}>Username</Text>
      <TextInput
        style={tailwind('h-10 border border-gray-300 mb-4 p-2')}
        value={username}
        onChangeText={setUsername}
        placeholder="Enter your username"
      />
      <Text style={tailwind('mb-2')}>Email</Text>
      <TextInput
        style={tailwind('h-10 border border-gray-300 mb-4 p-2')}
        value={email}
        onChangeText={setEmail}
        placeholder="Enter your email"
      />
      <Text style={tailwind('mb-2')}>Password</Text>
      <TextInput
        style={tailwind('h-10 border border-gray-300 mb-4 p-2')}
        value={password}
        onChangeText={setPassword}
        placeholder="Enter your password"
        secureTextEntry
      />
      <Button title="Signup" onPress={handleSignup} />
      <Button title="Go to Login" onPress={() => navigation.navigate('Login')} />
    </View>
  );
};

export default SignupScreen;
