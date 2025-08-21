import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function TextsScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Vente de Textes ✍️</Text>
      <Text>Publie ou achète des textes saisis facilement.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 16 },
  title: { fontSize: 20, fontWeight: 'bold', marginBottom: 8 }
});
