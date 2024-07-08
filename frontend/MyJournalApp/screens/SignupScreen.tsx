// components/SignupScreen.js

import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, Alert } from 'react-native';
import styled from 'styled-components/native';

const SignupScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignup = async () => {
    try {
      const response = await fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        throw new Error('Something went wrong');
      }

      const data = await response.json();
      Alert.alert('Success', `Message: ${data.message}`);
    } catch (error) {
      Alert.alert('Error', error.message);
    }
  };

  return (
    <Container>
      <Title>Sign Up</Title>
      <Input
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <Input
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button onPress={handleSignup}>
        <ButtonText>Sign Up</ButtonText>
      </Button>
      <SwitchAuth onPress={() => navigation.navigate('Login')}>
        <SwitchAuthText>Switch to Login</SwitchAuthText>
      </SwitchAuth>
    </Container>
  );
};

const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
`;

const Title = styled.Text`
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
`;

const Input = styled.TextInput`
  width: 80%;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  border: 1px solid #ccc;
  background-color: #fff;
`;

const Button = styled.TouchableOpacity`
  width: 80%;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  background-color: #007bff;
  align-items: center;
`;

const ButtonText = styled.Text`
  color: #fff;
  font-size: 18px;
`;

const SwitchAuth = styled.TouchableOpacity`
  margin-top: 20px;
`;

const SwitchAuthText = styled.Text`
  color: #007bff;
  font-size: 16px;
`;

export default SignupScreen;
