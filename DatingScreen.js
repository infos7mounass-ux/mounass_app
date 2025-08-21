import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function DatingScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Rencontres 💖</Text>
      <Text>Ici tu pourras découvrir et chatter avec d'autres personnes.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 16 },
  title: { fontSize: 20, fontWeight: 'bold', marginBottom: 8 }
});
