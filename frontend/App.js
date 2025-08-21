import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from './screens/HomeScreen';
import DatingScreen from './screens/DatingScreen';
import TextsScreen from './screens/TextsScreen';
import MarketplaceScreen from './screens/MarketplaceScreen';
import RealEstateScreen from './screens/RealEstateScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Accueil" component={HomeScreen} />
        <Tab.Screen name="Rencontres" component={DatingScreen} />
        <Tab.Screen name="Textes" component={TextsScreen} />
        <Tab.Screen name="Marketplace" component={MarketplaceScreen} />
        <Tab.Screen name="Immobilier" component={RealEstateScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
