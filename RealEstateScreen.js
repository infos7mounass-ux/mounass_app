import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function RealEstateScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Immobilier 🏠</Text>
      <Text>Trouvez des maisons à vendre ou à louer facilement.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 16 },
  title: { fontSize: 20, fontWeight: 'bold', marginBottom: 8 }
});
