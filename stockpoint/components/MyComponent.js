import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, ActivityIndicator, StyleSheet } from 'react-native';
import axios from 'axios';

const ApiDataComponent = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://ec2-3-87-211-227.compute-1.amazonaws.com/api/produtos/');
        setData(response.data);
      } catch (error) {
        console.error('Error:', error);
        setError('Não foi possível carregar os dados.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
        <Text>Carregando...</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.container}>
        <Text style={styles.errorText}>{error}</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dados recebidos da API:</Text>
      {Array.isArray(data) ? (
        <FlatList
          data={data}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <View style={styles.itemContainer}>
              <Text>Título: {item.title}</Text>
              <Text>Categoria: {item.categoria}</Text>
              <Text>Preço de Custo: R$ {item.cost_price}</Text>
              <Text>Preço de Venda: R$ {item.selling_price}</Text>
            </View>
          )}
        />
      ) : (
        <Text style={styles.data}>{JSON.stringify(data, null, 2)}</Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  data: {
    fontSize: 14,
    color: '#333',
    marginTop: 10,
  },
  errorText: {
    fontSize: 16,
    color: 'red',
  },
  itemContainer: {
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
    marginBottom: 5,
  },
});

export default ApiDataComponent;
