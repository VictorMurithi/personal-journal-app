import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { tailwind } from 'tailwind-rn';  // Import tailwind from tailwind-rn

const LoginScreen = ({ navigation }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await fetch('http://your-backend-url/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();
            if (response.ok) {
                if (data.access_token) {
                    navigation.navigate('Home');
                } else {
                    alert('Login failed');
                }
            } else {
                alert('Login failed');
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
            <Text style={tailwind('mb-2')}>Password</Text>
            <TextInput
                style={tailwind('h-10 border border-gray-300 mb-4 p-2')}
                value={password}
                onChangeText={setPassword}
                placeholder="Enter your password"
                secureTextEntry
            />
            <Button title="Login" onPress={handleLogin} />
            <Button title="Go to Signup" onPress={() => navigation.navigate('Signup')} />
        </View>
    );
};

export default LoginScreen;
